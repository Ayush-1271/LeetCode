class Solution:
    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
        n = len(nums)

        inv = 0
        diff = [0] * (n + 1)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    inv += 1

                    diff[i] += 1
                    diff[j + 1] -= 1

        need = 0
        active = 0

        for i in range(n):
            active += diff[i]

            if active > 0 and locked[i] == 1:
                need += 1

        if need > k:
            return -1

        return inv + need