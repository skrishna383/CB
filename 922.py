class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e,o=[],[]
        for i in nums:
            if i%2:
               o.append(i)
            else:
                e.append(i)
        ans=[]
        while e:
            ans.append(e.pop())
            ans.append(o.pop())
        return ans
#M2
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        es=[]
        os=[]
        for i in range(len(nums)):
            if i%2:
                if nums[i]%2==0:
                    os.append(i)
            if i%2==0:
                if nums[i]%2==1:
                    es.append(i)
            if es!=[] and os!=[]:
                e=es.pop()
                o=os.pop()
                nums[e],nums[o]=nums[o],nums[e]
        return nums