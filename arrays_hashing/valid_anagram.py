class Solution:
    #remember to add length check at the beginning
    #can use default instead of two if/elses
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        map1 = dict()
        map2 = dict()
        for x in range(len(s)): 
            map1[s[x]] = 1 + map1.get(s[x], 0)
            map2[t[x]] = 1 + map2.get(t[x], 0)
        return map1 == map2