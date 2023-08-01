class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l=0
        ans=0
        z=0
        for r in range(len(answerKey)):
            z=z+(answerKey[r]=='T')
            while z>k:
                z=z-(answerKey[l]=='T')
                l=l+1
            ans=max(ans,r-l+1)
        l=0
        z=0
        for r in range(len(answerKey)):
            z=z+(answerKey[r]=='F')
            while z>k:
                z=z-(answerKey[l]=='F')
                l=l+1
            ans=max(ans,r-l+1)
        return ans