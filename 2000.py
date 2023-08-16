class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if  ch not in word:
            return word
        else:    
            ans=""
            index=word.index(ch)
            index=index+1
            ans=word[:index][::-1]+word[index:]
            print(index)
            return ans