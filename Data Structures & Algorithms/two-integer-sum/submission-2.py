class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Two seperate integers in the array need to add to a target. 
        # Iterate through the list and add each element to a hash map
        # check if there exist a value that equals the current element 
        # at the key that represents that elements location in the array

        hashMap = {}
        answer =[]

        for i in range(len(nums)):
            
            remainderKey = target - nums[i]

            # We are searching up the value of the current element hoping that it matches the remainder
            # then taking that key's value which is the index of it
        
            if remainderKey not in hashMap:
                hashMap[nums[i]] = i
            else:
                answer.append(i)
                answer.append(hashMap[remainderKey])
                answer.sort()
                return answer

                

