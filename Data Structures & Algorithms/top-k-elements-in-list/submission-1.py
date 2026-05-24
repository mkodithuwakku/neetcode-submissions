
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # iterate through the list and put the elements as keys and their respective counts in the 
        # array as values. Then once done iterating take the k bins with the highest counts.

        HM = {}

        for num in nums:

            if num not in HM:
                HM[num] = 1
            else:
                HM[num] = HM[num] + 1
        
        answer = heapq.nlargest(k, HM.keys(), key= HM.get)
        
        return answer

