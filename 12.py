class Solution:
    def intToRoman(self, num: int) -> str:
        ans=''
        
        n=num
        print(n)
        d= n%10
        n=n//10
        print(n)
        r=''
        if d==1:
            r='I'
        elif d==2:
            r='II'    
        elif d==3:
            r='III'
        elif d==4:
            r='IV'
        elif d==5:
            r='V'
        elif d==6:
            r='VI'
        elif d==7:
            r='VII'
        elif d==8:
            r='VIII'
        elif d==9:
            r='IX'
        ans=ans+r
        r=''
        d= n%10
        n=n//10
        print(n)
        if d==1:
            r='X'
        elif d==2:
            r='XX'    
        elif d==3:
            r='XXX'
        elif d==4:
            r='XL'
        elif d==5:
            r='L'
        elif d==6:
            r='LX'
        elif d==7:
            r='LXX'
        elif d==8:
            r='LXXX'
        elif d==9:
            r='XC'
        ans=r+ans
        r=''
        d= n%10
        n=n//10
        print(n)
        if d==1:
            r='C'
        elif d==2:
            r='CC'    
        elif d==3:
            r='CCC'
        elif d==4:
            r='CD'
        elif d==5:
            r='D'
        elif d==6:
            r='DC'
        elif d==7:
            r='DCC'
        elif d==8:
            r='DCCC'
        elif d==9:
            r='CM'
        ans=r+ans
        r=''
        d= n%10
        n=n//10
        print(n)
        if d==1:
            r='M'
        elif d==2:
            r='MM'    
        elif d==3:
            r='MMM'
        ans=r+ans
        return ans