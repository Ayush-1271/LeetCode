#!/usr/bin/env python3
"""Generate the repository README from submitted LeetCode solutions."""
from __future__ import annotations
import json, re, sys, time
from collections import defaultdict
from pathlib import Path
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CACHE_PATH = ROOT / "data" / "problems.json"
README_PATH = ROOT / "README.md"
SOLUTION_SUFFIXES = {".py", ".cpp", ".cc", ".c", ".java", ".js", ".ts", ".go", ".rs", ".cs", ".kt", ".swift"}
DIR_PATTERN = re.compile(r"^(\d+)-(.+)$")
GRAPHQL_URL = "https://leetcode.com/graphql"
QUERY = """query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    title
    difficulty
    topicTags { name slug }
  }
}"""

def read_cache():
    try:
        data = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}

def fetch_metadata(slug):
    payload = json.dumps({"query": QUERY, "variables": {"titleSlug": slug}}).encode()
    request = Request(GRAPHQL_URL, data=payload, headers={
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/problems/{slug}/",
        "Origin": "https://leetcode.com",
        "User-Agent": "Mozilla/5.0 README-Generator/1.0",
    }, method="POST")
    try:
        with urlopen(request, timeout=15) as response:
            body = json.loads(response.read().decode("utf-8"))
        question = (body.get("data") or {}).get("question")
        if not question:
            return None
        return {
            "title": question.get("title"),
            "difficulty": question.get("difficulty"),
            "topics": [{"name": t["name"], "slug": t["slug"]}
                       for t in question.get("topicTags", []) if t.get("name") and t.get("slug")],
        }
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        print(f"Metadata unavailable for {slug}: {exc}", file=sys.stderr)
        return None

def fallback_metadata(folder, slug):
    title, difficulty = slug.replace("-", " ").title(), "Unknown"
    readme = folder / "README.md"
    if readme.exists():
        content = readme.read_text(encoding="utf-8", errors="replace")
        heading = re.search(r"<h2[^>]*>\s*<a[^>]*>(.*?)</a>", content, re.I | re.S)
        if heading:
            title = re.sub(r"<[^>]+>", "", heading.group(1)).strip()
        badge = re.search(r"(Easy|Medium|Hard)", content, re.I)
        if badge:
            difficulty = badge.group(1).title()
    return {"title": title, "difficulty": difficulty, "topics": []}

def collect_problems():
    cache, problems = read_cache(), []
    for folder in sorted(ROOT.iterdir(), key=lambda p: p.name.lower()):
        if not folder.is_dir():
            continue
        match = DIR_PATTERN.match(folder.name)
        if not match:
            continue
        problem_id, slug = match.groups()
        solutions = sorted(
            (p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in SOLUTION_SUFFIXES),
            key=lambda p: (p.suffix.lower() != ".py", p.name.lower()))
        if not solutions:
            continue
        metadata = cache.get(slug)
        if not isinstance(metadata, dict) or not metadata.get("topics"):
            fresh = fetch_metadata(slug)
            if fresh:
                metadata = fresh
                cache[slug] = fresh
                time.sleep(0.35)
        fallback = fallback_metadata(folder, slug)
        if not isinstance(metadata, dict):
            metadata = fallback
        problems.append({
            "id": int(problem_id), "slug": slug,
            "title": metadata.get("title") or fallback["title"],
            "difficulty": metadata.get("difficulty") or fallback["difficulty"],
            "topics": metadata.get("topics") or [],
            "solutions": [p.relative_to(ROOT).as_posix() for p in solutions],
        })
    return problems, cache

def make_readme(problems):
    difficulty_counts, topic_map = defaultdict(int), defaultdict(list)
    for problem in problems:
        difficulty_counts[problem["difficulty"]] += 1
        for topic in problem["topics"] or [{"name": "Uncategorized"}]:
            topic_map[topic["name"]].append(problem)
    lines = [
        "# LeetCode Solutions", "",
        "My LeetCode problem-solving repository. Solutions are primarily written in Python.", "",
        "## Progress", "", "| Metric | Count |", "|---|---:|",
        f"| Unique problems solved (solutions in this repository) | **{len(problems)}** |",
        f"| Topics attempted | **{len(topic_map)}** |",
        f"| Easy | {difficulty_counts['Easy']} |",
        f"| Medium | {difficulty_counts['Medium']} |",
        f"| Hard | {difficulty_counts['Hard']} |", "",
        "> A problem is counted once, even if it has multiple solution files or belongs to multiple topics.", "",
        "## Solutions by Topic", ""
    ]
    for topic in sorted(topic_map, key=str.casefold):
        entries = sorted(topic_map[topic], key=lambda p: (p["id"], p["title"].casefold()))
        lines.extend([f"### {topic} ({len(entries)})", ""])
        for p in entries:
            links = " · ".join(f"[{Path(path).name}]({path})" for path in p["solutions"])
            lines.append(f"- [**{p['title']}**](https://leetcode.com/problems/{p['slug']}/) — {p['difficulty']} · {links}")
        lines.append("")
    lines += ["---", "", "## Automation", "",
              "This README is generated by [scripts/generate_readme.py](scripts/generate_readme.py). "
              "GitHub Actions refreshes it when a solution is pushed.", "",
              "To regenerate locally: python scripts/generate_readme.py", ""]
    return "\n".join(lines)

def main():
    problems, cache = collect_problems()
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    README_PATH.write_text(make_readme(problems), encoding="utf-8")
    tagged_topics = {t["name"] for p in problems for t in p["topics"]}
    print(f"Generated README: {len(problems)} unique problems, {len(tagged_topics)} tagged topics.")

if __name__ == "__main__":
    main()
