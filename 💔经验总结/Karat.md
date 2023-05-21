1. 视频网站，任务是生成视频subtitle。现在只有一个机子一个process在工作，然后crash了。问有没有什么work around？ - 说可以多个机子一起process，或者用message asynchronously process，感觉答得不是很好


2. 有100,000个贩卖机分布全球，目前每天凌晨往server报status，然后有个job每天1AM处理status然后依此决定哪些要refill，问这样有什么问题 - 说全球机器同时发会造成拥堵，其它时候又是空闲的，感觉不合理。可以一天多几次report的时间，然后根据地域report时间段不同。

3. 用户储存photo的网站。目前是根据用户名来shard，问有什么问题 - 说会造成分布不均匀。问怎么解决 - 说了consistent hashing



https://productive-horse-bb0.notion.site/Roblox-Karat-2021-5-2022-2-9b07dcbba3634de080c3854c1293d0dc

```py
Text Justification
def fullJustify(self, words, maxWidth):
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > maxWidth:
            if len(cur) == 1:
                res.append( cur[0] + ' '*(maxWidth - num_of_letters) )
            else:
                num_spaces = maxWidth - num_of_letters
                space_between_words, num_extra_spaces = divmod( num_spaces, len(cur)-1)
                for i in range(num_extra_spaces):
                    cur[i] += ' '
                res.append( (' '*space_between_words).join(cur) )
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    res.append( ' '.join(cur) + ' '*(maxWidth - num_of_letters - len(cur) + 1) )
    return res
```

```py
repeated subarray

class Solution:  # 5520 ms, faster than 19.52%
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
                ans = max(ans, dp[i][j])
        return ans



```


```py

# valid soduku

def isValidSudoku(self, board):
    return (self.is_row_valid(board) and
            self.is_col_valid(board) and
            self.is_square_valid(board))

def is_row_valid(self, board):
    for row in board:
        if not self.is_unit_valid(row):
            return False
    return True

def is_col_valid(self, board):
    for col in zip(*board):
        if not self.is_unit_valid(col):
            return False
    return True

def is_square_valid(self, board):
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not self.is_unit_valid(square):
                return False
    return True

def is_unit_valid(self, unit):
    unit = [i for i in unit if i != '.']
    return len(set(unit)) == len(unit)

    ```

```py
valid parentheses

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
```

threads (of the same process) run in a shared memory space, while processes run in separate memory spaces.


```py
word search

'''
You are running a classroom and suspect that some of your students are passing around the answer to a multiple-choice question in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be either immediately below or immediately to the right of the previous letter.

Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates. If there are multiple matches, return any one.

grid1 = [
    ['b', 'b', 'b', 'a', 'l', 'l', 'o', 'o'],
    ['b', 'a', 'c', 'c', 'e', 's', 'c', 'n'],
    ['a', 'l', 't', 'e', 'w', 'c', 'e', 'w'],
    ['a', 'l', 'o', 's', 's', 'e', 'c', 'c'],
    ['w', 'o', 'o', 'w', 'a', 'c', 'a', 'w'],
    ['i', 'b', 'w', 'o', 'w', 'w', 'o', 'w']
]
word1_1 = "access"      # [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)]
word1_2 = "balloon"     # [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 7)]

word1_3 = "wow"         # [(4, 3), (5, 3), (5, 4)] OR
                        # [(5, 2), (5, 3), (5, 4)] OR
                        # [(5, 5), (5, 6), (5, 7)]

word1_4 = "sec"         # [(3, 4), (3, 5), (3, 6)] OR
                        # [(3, 4), (3, 5), (4, 5)]

word1_5 = "bbaal"       # [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]


grid2 = [
  ['a'],
]
word2_1 = "a"

grid3 = [
    ['c', 'a'],
    ['t', 't'],
    ['h', 'a'],
    ['a', 'c'],
    ['t', 'g']
]
word3_1 = "cat"
word3_2 = "hat"

grid4 = [
    ['c', 'c', 'x', 't', 'i', 'b'],
    ['c', 'a', 't', 'n', 'i', 'i'],
    ['a', 'x', 'n', 'x', 'p', 't'],
    ['t', 'x', 'i', 'x', 't', 't']
]
word4_1 = "catnip"      # [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4)] OR
                        # [(0, 1), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4)]


All test cases:

search(grid1, word1_1) => [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)]
search(grid1, word1_2) => [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 7)]
search(grid1, word1_3) => [(4, 3), (5, 3), (5, 4)] OR
                          [(5, 2), (5, 3), (5, 4)] OR
                          [(5, 5), (5, 6), (5, 7)]
search(grid1, word1_4) => [(3, 4), (3, 5), (3, 6)] OR
                          [(3, 4), (3, 5), (4, 5)]
search(grid1, word1_5) => [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]

search(grid2, word2_1) => [(0, 0)]

search(grid3, word3_1) => [(0, 0), (0, 1), (1, 1)]
search(grid3, word3_2) => [(2, 0), (3, 0), (4, 0)]

search(grid4, word4_1) => [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4)] OR
                          [(0, 1), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4)]

Complexity analysis variables:

r = number of rows
c = number of columns
w = length of the word
'''
grid1 = [
    ['b', 'b', 'b', 'a', 'l', 'l', 'o', 'o'],
    ['b', 'a', 'c', 'c', 'e', 's', 'c', 'n'],
    ['a', 'l', 't', 'e', 'w', 'c', 'e', 'w'],
    ['a', 'l', 'o', 's', 's', 'e', 'c', 'c'],
    ['w', 'o', 'o', 'w', 'a', 'c', 'a', 'w'],
    ['i', 'b', 'w', 'o', 'w', 'w', 'o', 'w'],
]
word1_1 = "access"
word1_2 = "balloon"
word1_3 = "wow"
word1_4 = "sec"
word1_5 = "bbaal"

grid2 = [
    ['a'],
]
word2_1 = "a"

grid3 = [
    ['c', 'a'],
    ['t', 't'],
    ['h', 'a'],
    ['a', 'c'],
    ['t', 'g'],
]
word3_1 = "cat"
word3_2 = "hat"

# grid4 = [
#     ['c', 'c', 'x', 't', 'i', 'b'],
#     ['c', 'a', 't', 'n', 'i', 'i'],
#     ['a', 'x', 'n', 'x', 'p', 't'],
#     ['t', 'x', 'i', 'x', 't', 't'],
# ]
# word4_1 = "catnip"




def solution2(grid, word):

    dirs = [[0,1],[1, 0]]

    def findWord(word, position, res):
        if len(word) > 0:
            char = word[0]
        else:
            return True
        [r, c] = position
        # print(word, grid[r][c], r, c, res) #a c 1 0
        if grid[r][c] == char:
            res += [(r, c)]
            found = False
            for d in dirs:
                new_position = [r + d[0], c + d[1]]
                # print( new_position)
                if 0 <= new_position[0] < len(grid) and 0 <= new_position[1] < len(grid[0]) and findWord(word[1:], new_position, res):
                    return True
                    # found = True
            # if found:
                # return True
        # early return if incorrect

        # find(word[1:], new_position)
        return False

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            res = []
            if findWord(word, [r, c], res):
               return res

    return res

grid4 = [
    ['c', 'c', 'x', 't', 'i', 'b'],
    ['c', 'a', 't', 'n', 'i', 'i'],
    ['a', 'x', 'n', 'x', 'p', 't'],
    ['t', 'x', 'i', 'x', 't', 't'],
]
word4_1 = "catnip"


print (solution2(grid1, word1_2))




# words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax", "baz"]
# note1 = "ctay"
# note2 = "bcanihjsrrrferet"
# note3 = "tbaykkjlga"
# note4 = "bbbblkkjbaby"
# note5 = "dad"
# note6 = "breadmaking"
# note7 = "dadaa"


# Time: O(W*S)
# Space: O(S)

def solution(words, note):
    import collections
    dic = collections.defaultdict(int)
    for char in note:
        dic[char] += 1

    for word in words:
        w_dic = collections.defaultdict(int)
        for char in word:
            w_dic[char] += 1

        is_valid = True
        for k in w_dic:
            if k in dic:
                if dic[k] < w_dic[k]:
                    is_valid =  False
            else:
                is_valid = False


        if is_valid:
            return word
    return "-"


# find(words, note1) # -> "cat"
# find(words, note2) #-> "cat"
# find(words, note3) #-> "-"
# find(words, note4) #-> "baby"
# find(words, note5) #-> "-"
# find(words, note6) #-> "bird"
# find(words, note7) #-> "dada"

# print (solution(words, note1))
# print (solution(words, note2))
# print (solution(words, note3))
# print (solution(words, note4))
# print (solution(words, note5))
# print (solution(words, note6))
# print (solution(words, note7))
```

```py


"""
While grading papers as an assistant, you've noticed some of them are surprisingly similar. You've decided to write a simple plagiarism detector to try to combat this, including checking for swapped in synonyms.

You've found a list of synonyms online. These synonyms come in a list of pairs, and sometimes you may have to link together multiple pairs to see if the words are synonyms.

In this example, "paper", "composition" and "essay" are all synonyms:
synonyms1_1 = [
  ("paper", "composition"),
  ("composition", "essay")
]
So these lines are considered equal:
line1_1 = "this paper is totally an original paper"
line1_2 = "this composition is totally an original essay"

similar(line1_1, line1_2, synonyms1_1) => True

Write a function that takes in two lines and a list of synonym pairs, and returns whether the two lines are considered equal.

Additional input data:
line2_1 = "the man in the blue shirt sat by the blue sea in a blue chair under the blue sky"
line2_2 = "the man in the teal shirt sat by the cerulean sea in a navy chair beneath the cyan sky"
synonyms2_1 = [("teal", "turquoise"), ("teal", "cyan"), ("cerulean", "navy"), ("blue", "navy"), ("navy", "teal"), ("under", "beneath")]
synonyms2_2 = [("teal", "turquoise"), ("teal", "cyan"), ("cerulean", "navy"), ("blue", "navy"), ("under", "beneath")]

Here is a diagram of how synonyms2_1 and synonyms2_2 connect together:

   ===synonyms2_1===            ===synonyms2_2===

   cerulean     blue            cerulean     blue
           \    /                       \    /
            navy                         navy
              |
            teal                         teal
           /    \                       /    \
    turquoise   cyan             turquoise   cyan

     under - beneath              under - beneath

With synonyms2_1, all of the instances of blue in the first sentence have synonyms in the second. However, without the (navy, teal) synonym, such as in synonyms2_2, blue would not be considered a synonym of teal, turquoise, and cyan, so with those synonyms we return False.

line3_1 = "also these sentences are not really related in any way"
line3_2 = "i like cats a lot but dogs are ok too"
synonyms3_1 = [("too", "also"), ("cats", "felines"), ("dogs", "canines")]

line4_1 = "it is important to play in spring"
line4_2 = "it is important to plow in spring"
synonyms4_1 = [("lay", "low"), ("spring", "springtime")]

Test Cases:
similar(line1_1, line1_2, synonyms1_1) => True
similar(line2_1, line2_2, synonyms2_1) => True
similar(line2_2, line2_1, synonyms2_1) => True
similar(line2_1, line2_2, synonyms2_2) => False
similar(line3_1, line3_2, synonyms3_1) => False
similar(line4_1, line4_2, synonyms4_1) => False

Complexity Variables:
N = length of the lines
S = number of synonym pairs
"""

line1_1 = "this paper is totally an original paper"
line1_2 = "this composition is totally an original essay"
synonyms1_1 = [
  ("paper", "composition"),
  ("composition", "essay")
]

line2_1 = "the man in the blue shirt sat by the blue sea in a blue chair under the blue sky"
line2_2 = "the man in the teal shirt sat by the cerulean sea in a navy chair beneath the cyan sky"
synonyms2_1 = [
  ("teal", "turquoise"),
  ("teal", "cyan"),
  ("cerulean", "navy"),
  ("blue", "navy"),
  ("navy", "teal"),
  ("under", "beneath")
]
synonyms2_2 = [
  ("teal", "turquoise"),
  ("teal", "cyan"),
  ("cerulean", "navy"),
  ("blue", "navy"),
  ("under", "beneath")
]

line3_1 = "also these sentences are not really related in any way"
line3_2 = "i like cats a lot but dogs are ok too"
synonyms3_1 = [
  ("too", "also"),
  ("cats", "felines"),
  ("dogs", "canines")
]

line4_1 = "it is important to play in spring"
line4_2 = "it is important to plow in spring"
synonyms4_1 = [
  ("lay", "low"),
  ("spring", "springtime")
]


class unionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        # print ("x ", x, self.parent)
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        # print("union", u, v, self.parent)
        # print( "find" , self.find(u),  self.find(v))
        pu, pv = self.find(u), self.find(v)
        print(pu, pv)
        if pu != pv:
            self.parent[pu] = pv
        print ("parent", self.parent)

def similar(line1, line2, syn):

    syn_word = set()
    syn_dict = dict()
    for word1, word2 in syn:
        syn_word.add(word1)
        syn_word.add(word2)

    syn_dict = {w: index for index, w in enumerate(syn_word)}

    uf = unionFind(len(syn_dict))

    for word1, word2 in syn:
        uf.union(syn_dict[word1], syn_dict[word2])

    line1w = line1.split(" ")
    line2w = line2.split(" ")
    for i in range(len(min(line1w, line2w))):
        w1, w2 = line1w[i], line2w[i]
        # print ("=", w1,w2)
        if w1 != w2:
            if (w1 not in syn_dict) or (w2 not in syn_dict):
                return False
            else:
                return uf.find(syn_dict[w1]) == uf.find(syn_dict[w2])

    return True

# synonyms1_1 = [
#   ("paper", "composition"),
#   ("composition", "essay")
# ]

# similar(line1_1, line1_2, synonyms1_1) => True
# similar(line2_1, line2_2, synonyms2_1) => True
# similar(line2_2, line2_1, synonyms2_1) => True
# similar(line2_1, line2_2, synonyms2_2) => False
# similar(line3_1, line3_2, synonyms3_1) => False
# similar(line4_1, line4_2, synonyms4_1) => False

print(similar(line2_1, line2_2, synonyms2_1) )
print(similar(line2_1, line2_2, synonyms2_2) )






def highest(courses):
# Excellent   E   5
# Great       G   4
# Average     A   3
# Fair        F   2
# Poor        P   1
# Incomplete  I   0
    grade_dic = {"E": 5, "G": 4, "A":3, "F": 2, "P": 1, "I": 0}
    result = 0
    max_credit = 0
    total_credit = 0
    for row in courses:
        r = row.split(",")
        credit = int(r[1])
        score = grade_dic[r[2]]
        result += credit * score
        if score != 5:
            max_credit = max(max_credit, credit)
        total_credit += credit
    return (result + max_credit)/total_credit


# highest(courses1) => 4.6
# highest(courses2) => 2.4285714285714284
# highest(courses3) => 5.0
# highest(courses4) => 2.066666666666667
# highest(courses5) => 2.0
# highest(courses6) => 1.2380952380952381

# print ("courses1", highest(courses1))
# print ("courses2", highest(courses2))
# print ("courses3", highest(courses3))
# print ("courses4", highest(courses4))
# print ("courses5", highest(courses5))
# print ("courses6", highest(courses6))
