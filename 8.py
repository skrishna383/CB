class Solution:
    def myAtoi(self, s: str) -> int:

        digits={
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9

        }
        ispositive=True
        str=s.strip()
        if str=="":
            return 0
        if str[0] in ('+','-'):
            if str[0]=='+':
                #str1=str.replace("+","")
                pass
            else:
                ispositive=False
                #str1=str.replace("-","")
            str1=str[1::]
        else:
            str1=str
        ans=0
        print(str1)
        for ch in str1:
            if ch in digits.keys():
                ans=ans*10+digits[ch]
            else :
                break
        #if ans > 2**31-1: return 2**31-1
        #if ans <- 2**31: return -2**31
        if ispositive :
            if ans > 2**31-1: return 2**31-1
            return ans
        else :
            if ans > 2**31: return -2**31
            return -ans

