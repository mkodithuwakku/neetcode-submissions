class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Iterate through once and get left values and put them. in an array
        #then iterate backwards and put them in their own array then multiply
        # Corresponding indices in both arrays
        leftOf = 1
        rightOf = 1
        leftArray = []
        rightArray = []
        output = []

        for i in range(0, len(nums)):

            if i != 0:
                leftOf = nums[i-1] * leftOf
            
            leftArray.append(leftOf)

        for i in range(len(nums)-1,-1,-1):

            if i != len(nums)-1:
                rightOf = nums[i+1] * rightOf
            
            rightArray.append(rightOf)
        
        for i in range(len(nums)):
            product = leftArray[i] * rightArray[len(nums)-1-i]
            output.append(product)
        
        return output


        

                




