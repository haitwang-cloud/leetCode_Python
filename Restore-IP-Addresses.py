class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def check(str):
            # ip不以0开头
            if str[0] == '0':
                return len(str) == 1
            else:
                return int(str) <= 255

        res = []
        if len(s) > 12:
            return res
        for i in range (len(s)):
            for j in range(i+1,len(s)):
                for k in range(j+1,len(s)-1):
                    s1=s[0:i+1]
                    s2=s[i+1:j+1]
                    s3=s[j+1:k+1]
                    s4=s[k+1:]
                    if check(s1) and check(s2) and check(s3) and check(s4):
                        res.append(s1+"."+s2+"."+s3+'.'+s4)
        return res
