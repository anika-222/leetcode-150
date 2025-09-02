class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        vals = set(nums)
        length = 0
        longest = 0
        for val in vals: 
            if (val-1) in vals:
                length = 1
            while(val+length) in vals:
                length += 1
            longest = max(length, longest)
        return longest
