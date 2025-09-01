class Solution:
    def productExceptSelf (self, nums:List[int]) -> List[int]:
        arr = [1]* (len(nums))
        prefix = 1 #product of all elements in num left of i in nums
        for i in range(len(nums)):
            arr[i] = prefix
            prefix *= nums[i] #1, 2, 3, 4 prefix = 1, 1, 2, 6
        postfix = 1
        for i in range(len(nums)-1, -1, -1): #multiply the numbers backwards in nums (postfix) and multiply that to arr
            arr[i] *= postfix
            postfix *= nums[i]
        return arr