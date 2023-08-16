class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<= 2:
            return 0
        ans=0
        l=0
        r=len(height)-1
        lmax=height[0]
        rmax=height[-1]
        while l<=r:
            if height[l]>lmax:
                lmax=height[l]
            if height[r]>rmax:
                rmax=height[r]
            if lmax<=rmax:
                ans=ans+lmax-height[l]
                l=l+1
            else:
                ans=ans+rmax-height[r]
                r=r-1
        return ans




