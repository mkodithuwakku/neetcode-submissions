class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # iterate through the strings and append some kind of length signifier
        # to the beginning of each one
        
        codeword = ""
        for string in strs:
            strLen = len(string)
            indicator = ":"
            codeStrings = str(strLen) + indicator + string
            codeword = codeword + codeStrings

        return codeword







    def decode(self, s: str) -> List[str]:
        #read through the combined string, find length identifiers
        # only take a slice of the length after that signifier

            output = []
            i = 0
            j = i
            
            while j < len(s):
                
                if s[j] == ":":
                    strLen = int(s[i:j])
                    codeword = s[j+1: j+strLen+1]
                    i = j + strLen + 1
                    output.append(str(codeword))
                    j = i - 1
                
                j = j + 1
            
            return output
            




        
