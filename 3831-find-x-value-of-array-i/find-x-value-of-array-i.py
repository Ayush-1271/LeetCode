class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:

        res = [0]*k
        prc = [0]*k

        for i in nums:
            crc = [0]*k
            r = i%k
            crc[r] += 1

            for j in range(k):
                nr = (j*r)%k
                crc[nr] +=prc[j]
            
            prc = crc

            for rem in range(k):
                res[rem] += prc[rem]
        return res