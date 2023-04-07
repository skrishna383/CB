from numpy import median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l =len(nums1)+len(nums2)
        isOdd=True
        mid=l/2
        if l%2==0:
            isOdd= False
            mid=mid+1          
        nums4=[]
        while len(nums4)<mid:
            if (len(nums1) != 0) and (len(nums2) != 0):
                if nums1[0]>nums2[0]:
                    nums4.append(nums2.pop(0))
                else:
                    nums4.append(nums1.pop(0))
            elif (len(nums1) == 0) and (len(nums2) == 0):
                break
            elif len(nums1) == 0:
                nums4.append(nums2.pop(0))
            elif len(nums2) == 0:
                nums4.append(nums1.pop(0))   
        if isOdd:
            return nums4[-1]
        else:
            return nums4[-1]/2+nums4[-2]/2