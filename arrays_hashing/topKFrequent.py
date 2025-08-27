class Solution:
    def topKFrequent(self, nums:List[int], k: int):
        map1 = dict()
        res = []
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            map1[num] = map1.get(num, 0) + 1
        for x, y in map1.items():
            freq[y].append(x)
        for z in range(len(freq)-1, 0 -1):
            for num in freq[z]:
                res.append(num)
                if len(res) == k:
                    return res