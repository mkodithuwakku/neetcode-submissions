class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        

        i, j = 0, len(heights)-1
        while i < j:
            area = (j - i) * min(heights[i], heights[j])

            if area > largest:
                largest = area
            
            if heights[i] < heights[j]:
                i = i + 1
            else:
                j = j -1
        return largest




