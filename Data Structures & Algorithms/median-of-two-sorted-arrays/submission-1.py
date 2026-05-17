class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        res = []
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                res.append(nums2[j])
                j += 1
            elif j == len(nums2):
                res.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        
        if len(res) % 2 == 0:
            i1 = (len(res) - 1) // 2
            i2 = i1 + 1
            return (res[i1] + res[i2]) / 2
        else:
            return res[len(res) // 2]



        

        