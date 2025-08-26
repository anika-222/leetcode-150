class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = dict()
        for word in strs:
            count= [0]*26
            for char in word:
                count[ord(char)- ord("a")]+=1
            if map1.get(tuple(count)) is not None:
                map1[tuple(count)].append(word)
            else: 
                map1[tuple(count)] = [word]
        return list(map1.values())
                
    # can use defaultdict too:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     map1 = defaultdict(list)
    #     for word in strs:
    #         count = [0]*26
    #         for char in word:
    #             count[ord(char)-ord("a")]+=1
    #         map1[tuple(count)].append(word)
    #     return list(map1.values())