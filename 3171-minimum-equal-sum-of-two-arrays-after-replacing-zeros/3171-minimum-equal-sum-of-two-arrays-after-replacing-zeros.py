class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_zeros, nums2_zeros = sum(1 for n1 in nums1 if n1 == 0), sum(1 for n2 in nums2 if n2 == 0)
        nums1_sum, nums2_sum = sum(nums1), sum(nums2)
        nums1_min, nums2_min = nums1_sum + nums1_zeros, nums2_sum + nums2_zeros
        ans = max(nums1_min, nums2_min)
        
        if (nums1_min > nums2_min and nums2_zeros == 0) or (nums2_min > nums1_min and nums1_zeros == 0):
            ans = -1
        
        return ans