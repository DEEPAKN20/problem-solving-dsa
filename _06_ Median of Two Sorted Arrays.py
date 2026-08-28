#https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=problem-list-v2&envId=array
#https://leetcode.com/submissions/detail/2123114427/
# 28 August 2026

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged_array = nums1 + nums2
        merged_array.sort()

        n = len(merged_array)

        if n % 2 == 1:
            median = merged_array[n // 2]
        else:
            median = (merged_array[n // 2 - 1] + merged_array[n // 2]) / 2

        return median

    """
    4 % 2 = 0 → even
    5 % 2 = 1 → odd
    6 % 2 = 0 → even
    Case 1: Odd number of elements
        [1, 2, 3, 4, 5]
                ↑
                3
         5 // 2 = 2
        index:   0  1  2  3  4
        value:   1  2  3  4  5
                        ↑
    Case 2: Even number of elements
    Suppose:
            [1, 2, 3, 4]
                ↑  ↑
                2  3
                indexes are:
                n // 2 - 1
                n // 2
                = (2 + 3) / 2
                = 2.5
                median = (merged_array[1] + merged_array[2]) / 2


    """

