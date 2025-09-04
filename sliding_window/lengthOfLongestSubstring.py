# solution only using pointers and sliding window
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         start = 0
#         next = 1
#         mLen = 0
#         if s:
#             seen = s[start]
#             mLen += 1
#             while next < len(s):
#                 if s[next] not in seen:
#                     seen+=s[next]
#                     newLen = len(seen)
#                     mLen = max(mLen, newLen) 
#                     next += 1
#                 else:
#                     start += 1
#                     next = start + 1
#                     seen = s[start]
#         return mLen
#solution using sliding windows and sets -  more efficient but both work 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        res = 0 
        charSet = set()
        for value in range(len(s)): #abcbcda cb start = 2 value = 3
            while s[value] in charSet:
                charSet.remove(s[start])
                start += 1
            charSet.add(s[value])
            res = max(res, value - start + 1)
        return res            