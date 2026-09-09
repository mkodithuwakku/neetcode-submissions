class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = 0
        
        hashMap = {}

        # iterate using index
        # for each number find the remainder and add it to hashMap
        # Firstly, check if that number exists in the hashmap as a key

        for index in range(len(nums)):
            rem = target - nums[index]

            if nums[index] in hashMap:
                output = []

                output.append(hashMap[nums[index]])
                output.append(index)

                return output
            
            hashMap[rem] = index
           



        