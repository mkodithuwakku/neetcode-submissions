class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # hashmap the nums and their counts

        countMap = {}

        for num in nums:

            if num in countMap:
                countMap[num] = countMap[num] + 1
            else:
                countMap[num] = 1
        
        output = []
        bucketMap = {}

        for num, count in countMap.items():
            if count in bucketMap:
                bucketMap[count].append(num)
            else:
                bucketMap[count] = [num]

        kCount = 0
        for i in range(len(nums), 0, -1):

            if i in bucketMap:
                output.extend(bucketMap[i])
                kCount = kCount + len(bucketMap[i])

                if kCount == k:
                    break
        
        return output

        




