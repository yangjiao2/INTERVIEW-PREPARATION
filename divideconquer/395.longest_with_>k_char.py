

# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:        
        if s == [] or k > len(s):
            return 0
        freq = collections.Counter(s)
        for i, char in enumerate(s):
            if freq[char] < k:
                return max(self.longestSubstring(s[:i], k),  self.longestSubstring(s[i+1:], k))
        return len(s)