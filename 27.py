class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:   
        j=0 
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[j]=nums[i]
                j=j+1
        return j
		
#M2
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums).