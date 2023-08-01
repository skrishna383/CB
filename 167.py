class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        j=0
        for i in numbers:
            d[i]=j
            j+=1
        if numbers.count(target/2)>1 :
            return (numbers.index(target/2)+1,numbers.index(target/2,numbers.index(target/2)+1)+1)
        for i in d.keys():
            index = d.get(target-i)
            if (index != None) & (index!=d.get(i)) :
                return [d.get(i)+1,index+1]


