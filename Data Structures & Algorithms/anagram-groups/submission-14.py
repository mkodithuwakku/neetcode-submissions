class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # iterate through list of strings
        # iterate through each string and create a map of it
        # make each char map a tuple and add it to the setMap
        # Have an output list
        # if the set does not exist in the output set then append it
        # if it does then append it to the correct index

        setMap = {}
        output = []
        for str in strs:
            charMap = {}
            for char in str:
                
                if char in charMap:
                    charMap[char] = charMap[char] + 1
                else : 
                    charMap[char] = 1

            tupledCharMap = tuple(sorted(charMap.items()))
                
            if tupledCharMap in setMap:
                setMap[tupledCharMap].append(str)
            else: 
                setMap[tupledCharMap] = [str]       


        output = list(setMap.values())
        return output




            