class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        sf=len(arr)
        def ps(arr,n):
            arr=arr[:n][::-1]+arr[n:]
            return arr
        while sf!=0:
            ind=arr.index(max(arr[:sf]))
            arr=ps(arr,ind+1)
            arr=ps(arr,sf)
            ans.append(ind+1)
            ans.append(sf)
            sf=sf-1
        return ans