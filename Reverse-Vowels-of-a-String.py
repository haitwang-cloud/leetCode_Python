class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        left,right=0,len(s)-1
        string_list=list(s)
        while left<=right:
            if string_list[left] not in vowels :
                left+=1
            elif string_list[right] not in vowels:
                right-=1
            else:
                tmp=string_list[left]
                string_list[left]=string_list[right]
                string_list[right]=tmp
                left+=1
                right-=1

        return ''.join(string_list)