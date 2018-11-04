# Time:  O(n)
# Space: O(1)


class Solution:
    def merge_1(self, nums1, m, nums2, n):
        i, j, index = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                index -= 1
                i -= 1
            else:
                nums1[index] = nums2[j]
                index -= 1
                j -= 1
        while j >= 0:
            nums1[index] = nums2[j]
            index -= 1
            j -= 1
    # 执行时间为36ms的案例

    def merge_2(self, nums1, m, nums2, n):
        k = len(nums1)
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[k-1] = nums1[m-1]
                m -= 1
            else:
                nums1[k-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
