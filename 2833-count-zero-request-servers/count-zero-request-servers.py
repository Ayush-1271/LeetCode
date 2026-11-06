class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs.sort(key=lambda a: a[1])
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        ans = [0] * len(queries)
        freq = {}

        left = right = 0
        active = 0

        for q, idx in sorted_queries:
            l = q - x

            # First add all logs up to current query time
            while right < len(logs) and logs[right][1] <= q:
                s = logs[right][0]

                if freq.get(s, 0) == 0:
                    active += 1

                freq[s] = freq.get(s, 0) + 1
                right += 1

            # Then remove logs before the window
            while left < right and logs[left][1] < l:
                s = logs[left][0]

                freq[s] -= 1

                if freq[s] == 0:
                    active -= 1
                    del freq[s]

                left += 1

            ans[idx] = n - active

        return ans