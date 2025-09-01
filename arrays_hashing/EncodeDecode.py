class Solution:
    def encode(self, strs:List[str]) -> str:
        x = ""
        for word in strs: 
            x += str(len(word)) + "#" + word 
        return x
    def decode(self, s:str) -> List[str]: 
        i = 0
        arr = []
        while i<len(s): 
            j = i
            while s[j] != "#":
                j +=1
                
            length = int(s[i:j])
            i = j+1
            j = i + length
            arr.append(s[i:j])
            i = j
        return arr
            
                
            