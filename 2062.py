class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        freq = {'a':0,'e':0,'i':0,'o':0,'u':0}
        ans=0
        c=0
        copy=freq.copy()
        l=0
        for i,w in enumerate(word):
            if w not in "aeiou":
                c=0
                l=i+1
                copy=freq.copy()
            else:
                copy[w]+=1
                while min(copy.values())!=0:
                    copy[word[l]]-=1
                    l=l+1
                    c=c+1
                ans=ans+c
        return ans
