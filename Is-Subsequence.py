# Time:  O(n)
# Space: O(1)

# Example 1:
# s = "abc", t = "ahbgdc"
#
# Return true.


class Solution:
    # 执行时间为362ms的案例
    def isSubsequence_1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return False
        index = 0
        for item in t:
            if item == s[index]:
                index += 1
            if index == len(s):
                break
        return index == len(s)
    # 执行时间为44ms的案例
    def isSubsequence_2(self, s, t):
        index=0
        for i in range(len(s)):#依据s进行搜索
            tmp=s[i] #当前需要搜索的字符为tmp
            try:
                res=t.index(tmp,index)
            except ValueError:#如果没找到返回错误
                return False
            else:
                index=res+1 #从j的下一个开始搜索
        #for循环结束，说明全部找到了
        return True
