class Solution:
    def isPalindrome(self, s: str) -> bool:
        index = 0
        reverseIndex = len(s) - 1
        s = s.lower()
        output = True
        
        while index <= reverseIndex:
            

            if s[index] == s[reverseIndex] and s[index].isalnum() == True and s[reverseIndex].isalnum() == True:
                index = index + 1
                reverseIndex =  reverseIndex - 1
            elif s[index].isalnum() == False:
                index = index + 1
            elif s[reverseIndex].isalnum() == False:
                reverseIndex =  reverseIndex - 1
            else:
                output = False
                break
        
        return output
            

        