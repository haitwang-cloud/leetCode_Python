class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers)==0:
            return [-1,-1]
        left,right=0,len(numbers)-1
        while(left<right):
            if numbers[left]+numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right]<target:
                left+=1
            elif numbers[left]+numbers[right]>target:
                right-=1