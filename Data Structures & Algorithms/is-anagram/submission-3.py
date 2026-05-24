class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        tMap = {}
        sMap = {}

        if len(s) == len(t):

            for char in s:
                if char in sMap:
                    sMap[char] = sMap[char] + 1
                else:
                    sMap[char] = 0
            
            for char in t:
                if char in tMap:
                    tMap[char] = tMap[char] + 1
                else:
                    tMap[char] = 0

            if tMap == sMap:
                return True
        
        return False
            
        