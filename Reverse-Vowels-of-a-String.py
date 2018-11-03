class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiou'
        strings = list(s)
        i, j = 0, len(strings)-1
        while i < j:
            if strings[i].lower() not in vowels:
                i += 1
            elif strings[j].lower() not in vowels:
                j -= 1
            else:
                strings[i], strings[j] = strings[j], strings[i]
                i += 1
                j -= 1
        return "".join(strings)
