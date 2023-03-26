class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r,a=0,len(height)-1,0
        while l<r:
            a=max(a,(r-l)*min(height[l],height[r]))
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return a