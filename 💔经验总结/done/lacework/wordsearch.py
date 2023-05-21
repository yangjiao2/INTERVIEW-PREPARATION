class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        res = ""
        for char in word:
            if char not in node.children:
                return None
            res += char
            node = node.children[char]
            if node.is_end:
                return res
        return None


def solution(s, words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    bold_tags = []
    n = len(s)
    i = 0
    while i < n:
        match = trie.search(s[i:])
        if match:
            bold_tags.append("<b>" + match + "</b>")
            i += len(match)
        else:
            bold_tags.append(s[i])
            i += 1

    return "".join(bold_tags)


# Example usage
s = "abcxyz123"
words = ["abc", "123"]
result = add_bold_tags(s, words)
print(result)
