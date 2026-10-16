class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        lazy = [0] * (4 * n)
        sums = [0] * (4 * n)
        squaredSums = [0] * (4 * n)

        def propagate(i, l, r):
            gap = r - l + 1
            L = lazy[i]

            squaredSums[i] = (
                squaredSums[i] + 2 * L * sums[i] + L * L * gap
            ) % MOD

            sums[i] = (sums[i] + L * gap) % MOD

            if l < r:
                lazy[2 * i + 1] += L
                lazy[2 * i + 2] += L

            lazy[i] = 0

        def update(i, start, end, l, r):
            if lazy[i] > 0:
                propagate(i, start, end)

            if end < l or start > r:
                return

            if start >= l and end <= r:
                lazy[i] = 1
                propagate(i, start, end)
                return

            mid = (start + end) // 2

            update(2 * i + 1, start, mid, l, r)
            update(2 * i + 2, mid + 1, end, l, r)

            sums[i] = (sums[2 * i + 1] + sums[2 * i + 2]) % MOD
            squaredSums[i] = (
                squaredSums[2 * i + 1] + squaredSums[2 * i + 2]
            ) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            update(0, 0, n - 1, prev + 1, i)

            ans = (ans + squaredSums[0]) % MOD
            last[x] = i

        return ans