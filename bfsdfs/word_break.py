
# "and" returns the first null value, or the last non-null value. so when tail == '', tail and ' ' gives you '', when len(tail) != 0, tail and ' ' gives you ' '.
def wordBreak(self, s, wordDict):
    memo = {len(s): ['']}
    def sentences(i):
        if i not in memo:
            memo[i] = [s[i:j] + (tail and ' ' + tail)
                    for j in range(i+1, len(s)+1)
                    if s[i:j] in wordDict
                    for tail in sentences(j)]
        print (i, memo)
        return memo[i]
    print (memo)
    return sentences(0)