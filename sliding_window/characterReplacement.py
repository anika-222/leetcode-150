class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxF = 0
        left = 0
        res = 0
        for right in range(len(s)): 
            count[s[right]] = 1 + count.get(s[right], 0)
            maxF = max(maxF, count[s[right]])
            while (right-left + 1) - maxF > k:
                count[left] -= 1 
                left += 1
            res = max(res, right - left + 1)
        return res
                