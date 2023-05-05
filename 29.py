class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend <0 and divisor >0 ) or (dividend >0 and divisor <0):
            sign =-1   
        else:
            sign =1
        if dividend<0:
            dividend=-dividend
        if divisor<0:
            divisor=-divisor
        q=0
        while dividend>=divisor:
            counter = 1
            decrement=divisor
            while dividend>=decrement:
                dividend =dividend-decrement
                q=q+counter
                counter=counter+counter
                decrement=decrement+decrement
        if sign*q >2**31-1 : return 2**31-1
        if sign*q <-2**31 : return -2**31
        return sign*q