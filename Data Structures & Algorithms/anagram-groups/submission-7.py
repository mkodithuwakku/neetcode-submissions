class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each string in the array, sort it and store the sorted version in the hash as the key,
        # and the value being the orignal string. Then print the has table at the end

        hashMap = {}

        for str in strs:
            sortedStr = "".join(sorted(str))

            if sortedStr in hashMap:
                hashMap[sortedStr].append(str)
            else:
                hashMap[sortedStr] = []
                hashMap[sortedStr].append(str)

        return list(hashMap.values())