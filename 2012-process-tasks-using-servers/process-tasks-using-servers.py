import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        
        n, ans = len(servers), []
        av = [(servers[j], j) for j in range(n)]
        heapq.heapify(av)

        busy = []
        t = 0
        
        for i, v in enumerate(tasks):
            t = max(t, i)

            while busy and busy[0][0] <= t:
                ft, w, j = heapq.heappop(busy)
                heapq.heappush(av, (w, j))

            if not av:
                t = busy[0][0]

                while busy and busy[0][0] <= t:
                    ft, w, j = heapq.heappop(busy)
                    heapq.heappush(av, (w, j))

            w, s = heapq.heappop(av)

            ans.append(s)

            # Update its next free time
            heapq.heappush(busy, (t + v, w, s))

        return ans
