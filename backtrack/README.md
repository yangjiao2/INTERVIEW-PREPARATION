
# Backtracking (NP-complete problems)

- eligibility:

Examples of CSP solved by Backtracking
- Permutations, Combinations, Subsets

- Boolean satisfiability problem (SAT)
- Hamiltonian path problem
- Travelling salesman problem
- Graph coloring

```
function backTrackAlgorithm(parameters) {
  function backtrack(startingState) {
    if (final condition is met) {
      add result;
    } else {
      loop from the starting state
        try a candidate;
        backtrack(adjustedStartingState);
        remove the candidate;
    }
  }

  handle edge cases
  initialize the result structure;
  backtrack(startingState);
  return result;
}

```
[古城](https://docs.google.com/presentation/d/1u12_iFmcm3e1Rn1bB7XYwMP90U_UwdLHQMrTDyK_AFs/edit#slide=id.gee2c1f06ac_0_161)

```
减枝的题目一般可以使用二分法去做，也相当于是增加了限制条件，这里不是二分部分，不详解
一些题目也可以用状态压缩dp来解决，比如人数少的时候，12个人的状态都压缩在一个intege里面，dfs+memo这里非dp也不详解
```


### 常见4把刀减枝方法
```
sort倒序，task先做大的这样可以累积时间先达到终止条件
global的result, 如果我们是求最小值，当过程中结果已经大于res的时候我们就直接停止
跳过重复的元素，类似permutation里面
改变搜索思路，单向遍历较多的task可以大幅提升速度。一般大的数据部分pointer单向递增，小数据的部分可以增加backtracking的遍历，比如i为task, backtrack每次for loop为session见最后一题。比如1434题帽子比人多，就单向帽子

```


Permutate with unique numbers


class Solution:
    """
    Level0: []
    level1: [1]                  [2]              [3]
    level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
    level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]

    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        self.backtracking(res,visited,[],nums)
        return res
    def backtracking(self,res,visited,subset,nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res,visited,subset+[nums[i]],nums)
                visited.remove(i)

