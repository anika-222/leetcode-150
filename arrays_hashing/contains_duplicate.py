class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateSet = set()
        isDuplicate = False
        for x in nums:
            if x in duplicateSet:
                isDuplicate = True
            duplicateSet.add(x)
        return isDuplicate
    #can also do return len(set(nums)) < len(nums)