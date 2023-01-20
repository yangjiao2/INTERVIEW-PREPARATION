----

Input:  "this is a test string"
Output:  string
Even length words are this, is, test, string. Even
maximum length word is string.

Input:  "geeksforgeeks is a platform for geeks"
Output:  platform
Only even length word is platform.

--

Missing words / Uncommon words

    def uncommonFromSentences(self, A, B):
        c = collections.Counter((A + " " + B).split())
        return [w for w in c if c[w] == 1]


---
