    #  The building popped out represent the height of a rectangle with the new building as the right boundary and the current stack top as the left boundar
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in xrange(len(height)):
            while stack and height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans
