#brute force solution
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         arr = []
#         for num in range(len(numbers)-1):
#             j = num + 1
#             needed = target - numbers[num]
#             while j < len(numbers):
#                 if numbers[j] == needed:
#                     arr.append(num+1)
#                     arr.append(j+1)
#                 j += 1
#         return arr

from typing import List

class Solution:
    def twoSumPointers(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start<end :
            if (numbers[start] + numbers[end]) < target:
                start += 1
            elif (numbers[end] + numbers[start]) > target:
                end -= 1
            else: 
                return [start + 1, end + 1]
        return []