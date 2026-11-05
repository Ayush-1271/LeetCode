class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less = []
        greater = []
        equal = []
        for i in nums:
            if i<pivot:
                less.append(i)
            elif i>pivot:
                greater.append(i)
            else:
                equal.append(i)
        
        return less+equal+greater