class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)

        pos = {v: i + 1 for i, v in enumerate(vals)}

        count = [0] * (m + 1)
        sums = [0] * (m + 1)

        def update(bit, i, delta):
            while i <= m:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        def kth(q):
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= m and count[nxt] < q:
                    idx = nxt
                    q -= count[nxt]
                step >>= 1

            return idx + 1

        def add(v, delta):
            p = pos[v]
            update(count, p, delta)
            update(sums, p, v * delta)

        def get_cost():
            mid = kth((x + 1) // 2)
            median = vals[mid - 1]

            left_count = query(count, mid)
            left_sum = query(sums, mid)

            right_count = x - left_count
            right_sum = total - left_sum

            return (median * left_count - left_sum +
                    right_sum - median * right_count)

        # Calculate cost of every window
        for v in nums[:x]:
            add(v, 1)

        total = sum(nums[:x])
        costs = []

        for i in range(n - x + 1):

            costs.append(get_cost())

            if i < n - x:
                add(nums[i], -1)
                add(nums[i + x], 1)
                total += nums[i + x] - nums[i]

        # DP
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):

            curr = [INF] * (n + 1)

            for i in range(1, n + 1):

                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]