class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set()
        streak = 1
        longStreak = 0
        # Get nums[i] - 1 into a set
        for num in nums:
            numSet.add(num)
            
        # For each number in the list check what the longest streak is and update
        startSet = set()
        for num in nums:
            streak = 1
            if num - 1 not in numSet and num not in startSet:
                startSet.add(num)
                while num+1 in numSet:
                    streak = streak + 1
                    num = num + 1
            
                if streak > longStreak:
                        longStreak = streak
                
                    
        
        return longStreak