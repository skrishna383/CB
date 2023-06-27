class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        da=[amount+1]*(amount+1)
        da[0]=0
        for a in range(1,amount+1):
            for c in coins:
                if a-c>=0:
                    da[a]=min(da[a],1+da[a-c])
        if da[amount]!=amount+1:
            return da[amount]
        else:
            return -1