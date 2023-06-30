class Solution:
    def climbStairs(self, n: int) -> int:
        nxt=1
        far=1
        for i in range(n-1):
            temp=nxt+far
            far=nxt
            nxt=temp
#            nxt,far=nxt+far,nxt
        return nxt
