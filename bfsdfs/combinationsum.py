class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def dfs(cand, target, path, res):
            # print ("cand, target, path, res", cand, target, path, res)
            if target == 0:
                res.append(path)
            elif target < 0:
                return

            for i in range( len(cand)):
                if i > 0 and cand[i] == cand[i-1]: continue
                c = cand[i]
                # print (i, res, target - c, cand)

                dfs(cand[i+ 1: ], target - c, path+ [c], res)

        dfs(candidates, target, [], res)
        return res


    # class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(idx, path, cur):
            if cur > target: return
            if cur == target:
                res.append(path)
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1, path+[candidates[i]], cur+candidates[i])
        dfs(0, [], 0)
        return res
