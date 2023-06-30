class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a0,a1,a2=0,0,0
        for i in nums:
          if i ==0 :
            a0=a0+1
          elif i==1:
            a1=a1+1
          else:
            a2=a2+1
        if a0 !=0:
          for i in range(0,a0):
            nums[i]=0
        if a1 !=0:
          for i in range(a0,a1+a0):
            nums[i]=1
        if a2 !=0:
          for i in range(a1+a0,a1+a2+a0):
            nums[i]=2
                              

