class Solution(object):
    # 执行时间为664ms的案例
    def ladderLength_1(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        distance, cur, visited, lookup = 0, [
            beginWord], set([beginWord]), set(wordList)

        while cur:
            next_queue = []

            for word in cur:
                if word == endWord:
                    return distance + 1
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in lookup:
                            next_queue.append(candidate)
                            visited.add(candidate)
            distance += 1
            cur = next_queue

        return 0
    # 执行时间为108ms的案例
    def ladderLength(self, beginWord, endWord, wordList):

        wordSet = set(wordList)
        headQ = set([beginWord])
        tailQ = set([endWord])
        step = 1

        if endWord not in wordSet:
            return 0
        else:
            wordSet.discard(endWord)

        while headQ:
            step += 1
            currSet = set()
            for word in headQ:
                for i in range(len(word)):
                    p1 = word[:i]
                    p2 = word[i + 1:]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new = p1 + c + p2
                        if new in tailQ:
                            return step
                        if new in wordSet:
                            currSet.add(new)
                            wordSet.remove(new)

            headQ = currSet
            if len(headQ) > len(tailQ):
                headQ, tailQ = tailQ, headQ

        return 0
