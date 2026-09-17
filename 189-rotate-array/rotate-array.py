class Solution:
    
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr, start, end):
            while start<end:
                arr[start], arr[end] = arr[end], arr[start]
                start+=1
                end-=1
            return arr
        
        n = len(nums)
        k = k%n
        if n == 0 or k==0:
            return nums
        
        nums = reverse(nums, 0, n-1)
        nums = reverse(nums, 0, k-1)
        nums = reverse(nums, k, n-1)

        return nums
        