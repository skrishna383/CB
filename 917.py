class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ascii_list1 = list(string.ascii_lowercase)
        ascii_list2 = list(string.ascii_uppercase)
        ascii_list=ascii_list1+ascii_list2
        a=''
        ind=0
        for i in s:
            if i in ascii_list:
                a=a+i
        ans=""
        for i in range(len(s)):
            if s[i] in ascii_list:
                ans=ans+a[::-1][ind]
                ind=ind+1
            else:
                ans=ans+s[i]
        return ans