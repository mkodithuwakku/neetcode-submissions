class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create hash to store first characters then check if the hashes are equal

        sHash = {}
        tHash = {}

        for char in s:

            if sHash.get(char) != None:
                sHash[char] = sHash[char] + 1
            else: 
                sHash[char] = 0

        for char in t:

            if tHash.get(char) != None:
                tHash[char] = tHash[char] + 1
            else: 
                tHash[char] = 0
        
        if tHash != sHash:
            return False
        else:
            return True

        
        

            