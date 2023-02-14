
# Time: O(N * 26M * M), where M <= 10 is the length of each word and N <= 500 is the total number of words in the input word list
# Space: O(M * N)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        wordSet.remove(beginWord)

        def neighbors(s):
            for i in range(len(s)):
                chars = list(s)
                for c in ascii_lowercase:
                    chars[i] = c
                    newStr = "".join(chars)
                    if newStr in wordSet:
                        yield newStr

        ans = 0
        q = deque([beginWord])
        while q:
            ans += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return ans

                for newStr in neighbors(cur):
                    q.append(newStr)
                    wordSet.remove(newStr)

        return 0  # no such transformation sequence.

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.append(beginWord)
        m, n = len(wordList[0]), len(wordList)
        words_inverse = {w:i for i, w in enumerate(wordList)}

        words_graph = defaultdict(set)
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        if endWord not in words_inverse: return 0
        end_ind = words_inverse[endWord]

        for word in wordList:
            for l in range(m):
                p1, p2 = word[0:l], word[l+1:]
                for i in alphabet:
                    tmp = p1 + i + p2
                    if tmp in words_inverse and tmp != word:
                        words_graph[words_inverse[word]].add(words_inverse[tmp])

        depths = [-1] * (n-1) + [0]
        queue = deque([n-1])

        while queue:
            curr = queue.popleft()
            if curr == end_ind:
                return depths[end_ind]  + 1
            for neib in words_graph[curr]:
                if depths[neib] == -1:
                    queue.append(neib)
                    depths[neib] = depths[curr] + 1

        return 0

# bi-directional

# https://leetcode.com/problems/word-ladder/solutions/40711/two-end-bfs-in-java-31ms/
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        # wordSet.remove(beginWord)

        def getNeighbors(s):
            res = []
            # print ('wordSet', wordSet)
            for i in range(len(s)):
                chars = list(s)
                for c in ascii_lowercase:
                    chars[i] = c
                    newStr = "".join(chars)
                    # print ('newStr', newStr)
                    if newStr in wordSet:
                        res += newStr,
            return res

        def update(queue, visit, oppovisit, count):
            for _ in range(len(queue)):
                cur = queue.popleft()
                # if cur == endWord:
                #     return ans
                print ( cur, oppovisit, cur in oppovisit, count)
                if cur in oppovisit:
                    self.ans = count + oppovisit[cur] - 1

                    return queue, visit
                neighbors = getNeighbors(cur)
                for n in neighbors:
                    print ('n' , n)
                    if n not in visit:
                        queue.append(n)
                        # wordSet.remove(n)
                        visit[n] = count + 1
            return queue, visit

        if endWord not in wordList:
            return 0
        self.ans = None
        q = deque([beginWord])
        q2 = deque([endWord])

        m, n = 1, 1
        v = {beginWord: m}
        v2 = {endWord: n}

        while q and q2 and self.ans is None:
            if len(q) < len(q2):
                q, v = update(q, v, v2, m)
                m += 1
            else:
                q2, v2 = update(q2, v2, v, n)
                n += 1
            print (q, v, q2, v2)


        return self.ans if self.ans is not None else 0  # no such transformation sequence.
