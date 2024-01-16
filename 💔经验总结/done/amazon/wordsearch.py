class TrieNode:
    def __init__(self):
        self.ch = ''
        self.stop = False
        self.children = {}

    def contains_child(self, c):
        return c in self.children

    def put_child(self, c):
        self.children[c] = TrieNode(c)

    def get_child(self, c):
        return self.children[c]

    def set_stop(self, b):
        self.stop = b

    def get_stop(self):
        return self.stop

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return

        tmp = self.root
        for ch in word:
            if ch not in tmp.children:
                tmp.put_child(ch)
            tmp = tmp.get_child(ch)
        tmp.set_stop(True)

    def search(self, word):
        if not word:
            return True

        tmp = self.root
        for ch in word:
            if ch not in tmp.children:
                return False
            tmp = tmp.get_child(ch)

        return tmp.get_stop()

    def starts_with(self, word):
        if not word:
            return True

        tmp = self.root
        for ch in word:
            if ch not in tmp.children:
                return False
            tmp = tmp.get_child(ch)

        return True

class Solution:
    def findWords(self, b, ws):
        res = []
        if not b or not ws or len(b) == 0 or len(b[0]) == 0 or len(ws) == 0:
            return res

        r = Trie()
        for s in ws:
            r.insert(s)

        M = len(b)
        N = len(b[0])
        v = [[False for _ in range(N)] for _ in range(M)]
        for i in range(M):
            for j in range(N):
                self.word_search(b, r.root, v, i, j, "", res)
        return res

    def word_search(self, b, root, v, i, j, string, res):
        M = len(b)
        N = len(b[0])
        if i < 0 or i >= M or j < 0 or j >= N or v[i][j] or not root.contains_child(b[i][j]):
            return

        string += b[i][j]
        if root.get_child(b[i][j]).get_stop():
            res.append(string)
            return

        v[i][j] = True
        self.word_search(b, root.get_child(b[i][j]), v, i + 1, j, string, res)
        self.word_search(b, root.get_child(b[i][j]), v, i + 1, j+1, string, res)
        self.word_search(b, root.get_child(b[i][j]), v, i , j+1, string, res)
        self.word_search(b, root.get_child(b[i][j]), v, i-1, j+1, string, res)
        self.word_search(b, root.get_child(b[i][j]), v, i-1, j, string, res)
        self.word_search(b, root.get_child(b[i][j]), v, i-1, j - 1, string, res)
        self.word_search(b, root.get_child(b[i][j]), v, i, j - 1, string, res)
        self.word_search(b, root.get_child(b[i][j]), v, i+1, j - 1, string, res)
        v[i][j] = False

# Example usage:
# sol = Solution()
# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
# words = ["oath","pea","eat","rain"]
# result = sol.findWords(board, words)
# print(result)