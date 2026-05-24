class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    # Determine if integers in the integer array appear more than once
    # Iteratively use set 

        IntSet = set()

        for num in nums:

            if num in IntSet:
                return True
            else:
                IntSet.add(num)
        return False


        