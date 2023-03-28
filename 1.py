class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        j=0
        for i in nums:
            d[i]=j
            j+=1
        if nums.count(target/2)>1 :
            return (nums.index(target/2),nums.index(target/2,nums.index(target/2)+1))
        for i in d.keys():
            index = d.get(target-i)
            if (index != None) & (index!=d.get(i)) :
                return [index,d.get(i)]



