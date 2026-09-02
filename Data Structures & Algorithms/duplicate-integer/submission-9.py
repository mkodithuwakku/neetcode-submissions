class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        theSet = set()

        for index in range(len(nums)):

            if nums[index] in theSet:
                return True
            else:
                theSet.add(nums[index])
        
        return False

        
        