class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = {}

        # Iterate through strs
        for string in strs:
            key = ''.join(sorted(string))
            
            if key not in hashMap:
                    hashMap[key] = []
            hashMap[key].append(string)

        
        return list(hashMap.values())



        # Sort each entry alphabetically and add it to hash

        # If entry exists in hash then add it to the same bucket

        # Print every bucket

        