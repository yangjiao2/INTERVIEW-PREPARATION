# start and end

class Solution:
# @param {integer[]} nums1
# @param {integer[]} nums2
# @return {float}
def find(self, nums1, s1, e1, nums2, s2, e2, k):
    if e1 - s1 < 0:
        return nums2[k + s2]
    if e2 - s2 < 0:
        return nums1[k + s1]
    if k < 1:
        return min(nums1[k + s1], nums2[k + s2])
    ia, ib = (s1 + e1) // 2 , (s2 + e2) // 2
    ma, mb = nums1[ia], nums2[ib]
    if (ia - s1) + (ib - s2) < k:
        if ma > mb:
            return self.find(nums1, s1, e1, nums2, ib + 1, e2, k - (ib - s2) - 1)
        else:
            return self.find(nums1, ia + 1, e1, nums2, s2, e2, k - (ia - s1) - 1)
    else:
        if ma > mb:
            return self.find(nums1, s1, ia - 1, nums2, s2, e2, k)
        else:
            return self.find(nums1, s1, e1, nums2, s2, ib - 1, k)

def findMedianSortedArrays(self, nums1, nums2):
    l = len(nums1) + len(nums2)
    if l % 2 == 1:
        return self.find(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, l // 2)
    else:
        return (self.find(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, l // 2) + self.find(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, l // 2 - 1)) / 2.0
