#can use enumerate to form a value to index hashmap 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = dict()
        for i, n in enumerate(nums):
            needed = target - n
            if map1.get(needed)!=None:
                return [map1.get(needed), i]
            else:
                map1[n] = i
    
    

# my original solution
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#         map1 = dict()
#         found = []
#         for x in range(len(nums)):
#             needed = target - nums[x]
#             if map1.get(needed) == None:
#                 map1[nums[x]] = x
#             else:
#                 found1 = map1.get(needed)
#                 found = [found1, x]
#                 break
#                 #add break to save time
#         return found