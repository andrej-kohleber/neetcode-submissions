class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        #[1, 2, 4, 6] 
        # 1  1  2  8
        # 48 24 6  1
        # 48 24 12 8
        
        nums1 = [1] + list(nums)
        for i in range(1, len(nums1) - 1):
            nums1[i] *= nums1[i - 1]

        nums1 = nums1[:-1]

        nums2 = list(nums) + [1]
        for i in range(len(nums2) - 2, -1, -1):
            nums2[i] *= nums2[i + 1]

        nums2 = nums2[1:]

        for i in range(len(nums)):
            nums[i] = nums1[i] * nums2[i]

        return nums
        

        

        