[link](https://leetcode.com/discuss/general-discussion/458695/Dynamic-Programming-Patterns)
1. [Minimum (Maximum) Path to Reach a Target](#1-minimum-maximum-path-to-reach-a-target)
2. [Distinct ways](#2-distinct-ways)

# 1. Minimum (Maximum) Path to Reach a Target

```
routes[i] = min(routes[i-1], routes[i-2], ... , routes[i-k]) + cost[i]

```

### steps:

Top-Down
```java
for (int j = 0; j < ways.size(); ++j) {
    result = min(result, topDown(target - ways[j]) + cost/ path / sum);
}
return memo[/*state parameters*/] = result;
```
Bottom-Up
```java
dp = [math.inf] * (amount + 1)
dp[0] = 0
for (int i = 1; i <= target; ++i) {
   for (int j = 0; j < ways.size(); ++j) {
       if (ways[j] <= i) {
           dp[i] = min(dp[i], dp[i - ways[j]] + cost / path / sum) ;
       }
   }
}

return dp[target]

```py
if r == 0 and c == 0:
    continue
grid[r][c] = min(
    grid[r][c]  + (grid[r][c-1] if c > 0 else math.inf),
    grid[r][c] +  (grid[r-1][c] if r > 0 else math.inf))
```

top-down due to unclear starting point (HP)

NOTE: added dummy boundary and update `dp[m-1][n], dp[m][n-1]` due to requirements in the ending `dp[m][n]` should be at least 1

```py
        dp = [[float("inf")]*(n+1) for _ in range(m+1)]
        dp[m-1][n], dp[m][n-1] = 1, 1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)


```

```py
    ## pay attention to initiation
    # base case initialization
	dp[0] = 1
	dp[1] = 0 if s[0] == "0" else 1   #(1)


	for i in range(2, len(s) + 1):
		# One step jump
		if 0 < int(s[i-1:i]) <= 9:    #(2)
			dp[i] += dp[i - 1]
		# Two step jump
		if 10 <= int(s[i-2:i]) <= 26: #(3)
			dp[i] += dp[i - 2]

```


## example
[coin change](./322_coin-change.py)
[decode ways](./91_decode-ways.py)
[]

# 2. Distinct ways


### steps:

1. initialize and sort (greedy)

2. loop through possible answers
    1) get eligible value
    - check with result (prune if already not in answer boundary, e.g: min, max step )
    - check if arrangement is duplicated (prune since order does not matter, e.g: sum of worker)
    2) append possible answer
    3) dfs
    4) remove possible answer
    5) add new branch


general approach to backtracking questions in Java (Subsets, Permutations, Combination Sum:
https://leetcode.com/problems/combination-sum/solutions/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)/


## example
Permutation ii


https://leetcode.com/problems/permutations-ii/solutions/18602/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others/?orderBy=most_votes


```py

# Below is an iterative solution:

    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in xrange(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break              #handles duplication
            ans = new_ans
        return ans

# Below is a backtracking solution:

    from collections import Counter
    def permuteUnique(self, nums):
        def btrack(path, counter):
            if len(path)==len(nums):
                ans.append(path[:])
            for x in counter:  # dont pick duplicates
                if counter[x] > 0:
                    path.append(x)
                    counter[x] -= 1
                    btrack(path, counter)
                    path.pop()
                    counter[x] += 1
        ans = []
        btrack([], Counter(nums))
        return ans

```
