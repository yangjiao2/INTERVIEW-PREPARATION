        def swap(p1, p2):
            tmp = nums[p2]
            nums[p2] = nums[p1]
            nums[p1] = tmp

        length = len(nums)
        if length == 0:
            return
        left = 0
        right = length - 1
        p = 0
        while p <= right:
            if nums[p] < 1:
                # the value at left must be equal or smaller than 1
                swap(left, p)
                p += 1
                left += 1
            elif nums[p] == 1:
                p += 1
            else:
                # don't increment p here, cause you don't know the swapped value
                swap(right, p)
                right -= 1
