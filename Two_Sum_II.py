class Solution:
    def twoSum_1(self, numbers: List[int], target: int) -> List[int]:
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
    def twoSum_2(self, numbers: List[int], target: int) -> List[int]:
        # 继续采用hashmap的思想
        hashmap = {}
        for index, num1 in enumerate(numbers):
            num2 = target - num1

            if num2 in hashmap:
                return [hashmap[num2] + 1, index + 1]

            hashmap[num1] = index