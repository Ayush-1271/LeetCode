class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {c:i for i, c in reversed(list(enumerate(s)))} 
        last = {c:i for i, c in enumerate(s)}

        def valid(i):
            r = last[s[i]]
            j = i
            while j <= r:
                if first[s[j]] <i:
                    return -1
                r = max(r, last[s[j]])
                j+=1
            return r
        
        seq = []
        for i in range(len(s)):
            if i == first[s[i]]:
                v_r = valid(i)
                if v_r != -1:
                    seq.append((v_r, i))
        seq.sort()
        ans, l_e = [], -1
        for e, st in seq:
            if st>l_e:
                ans.append(s[st:e+1])
                l_e = e
        return ans