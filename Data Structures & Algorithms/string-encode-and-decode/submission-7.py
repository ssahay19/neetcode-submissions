class Solution:

    def encode(self, strs: List[str]) -> str:
        res = " "
        for s in strs:
            res += str(len(s))
            res += "#" 
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        length = ""
        i = 0
        while i < len(s):
            if s[i] != "#":
                length+=s[i]
                i+=1
            else:
                length = int(length)
                word = s[i+1:i+1+length]
                res.append(word)
                i=i+1+length
                length=""
             
        return res