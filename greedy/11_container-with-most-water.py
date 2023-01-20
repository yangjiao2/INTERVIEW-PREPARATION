class Solution:
    def maxArea(self, height: List[int]) -> int:
        ## greedy
        l, r = 0, len(height)-1
        lmax, rmax = 0, 0
        res = 0
        while l < r:
            lmax, rmax = max(lmax, height[l]), max(height[r], rmax)
            res = max(res, (r-l) * min(lmax, rmax) )
            if (height[l] > height[r]):
                r -= 1
            else:
                l += 1
            print (lmax, rmax ,min(lmax, rmax), l, r, res, max(res, (l-r)))
        return res
