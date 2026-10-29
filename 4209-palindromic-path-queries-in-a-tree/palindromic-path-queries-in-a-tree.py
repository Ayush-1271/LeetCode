
from typing import List

class Solution:
    def palindromePath(
        self,
        n: int,
        edges: List[List[int]],
        s: str,
        queries: List[str]
    ) -> List[bool]:

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Step 1: Find parent, depth, and traversal order
        parent = [-1] * n
        depth = [0] * n
        order = [0]
        parent[0] = 0

        for u in order:
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)

        # Step 2: Calculate subtree sizes and heavy children
        size = [1] * n
        heavy = [-1] * n

        for u in reversed(order):
            largest = 0

            for v in adj[u]:
                if parent[v] == u:
                    size[u] += size[v]

                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        # Step 3: Heavy-Light Decomposition
        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in adj[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        # Step 4: Segment tree with XOR masks
        base = 1
        while base < n:
            base *= 2

        seg = [0] * (2 * base)

        for u in range(n):
            seg[base + pos[u]] = 1 << (ord(s[u]) - ord('a'))

        for i in range(base - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        # Point update
        def update(p, value):
            p += base
            seg[p] = value
            p //= 2

            while p:
                seg[p] = seg[2 * p] ^ seg[2 * p + 1]
                p //= 2

        # Inclusive range XOR query
        def range_xor(l, r):
            l += base
            r += base
            result = 0

            while l <= r:
                if l & 1:
                    result ^= seg[l]
                    l += 1

                if not (r & 1):
                    result ^= seg[r]
                    r -= 1

                l //= 2
                r //= 2

            return result

        # XOR mask of every node on the path u -> v
        def path_xor(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(pos[head[u]], pos[u])
                u = parent[head[u]]

            l = min(pos[u], pos[v])
            r = max(pos[u], pos[v])
            result ^= range_xor(l, r)

            return result

        chars = list(s)
        answer = []

        # Step 5: Process queries
        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                chars[u] = c
                mask = 1 << (ord(c) - ord('a'))
                update(pos[u], mask)

            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_xor(u, v)

                # At most one character can have odd frequency
                answer.append((mask & (mask - 1)) == 0)

        return answer
