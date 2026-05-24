class Solution:

    def encode(self, strs: List[str]) -> str:
        # Create an encoder where the length of the str slice is appended before the string,
        # along with an indicator(in this case :)
        # Ex) [axe, at] = 3:axe2:at
        # Then they are all combined and returned as a single string
        codeword = ""

        for string in strs:
            stringLength = len(string)
            codeword += str(stringLength)
            codeword += ":"
            codeword += string

            
        #print(codeword)
        return codeword

            

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        # go through each char in the string
        # use regex to find number^ combinations
        # once one is identified create inner loop at start of word to end and append to answer
        while i < len(s):
            j = i

            while s[j] != ":":
                j += 1
            
            length = int(s[i:j])

            ans.append(s[j+1:j+1+length])

            i = j + 1 + length


           

        return ans