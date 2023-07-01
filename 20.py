class Solution:
    def isValid(self, s: str) -> bool:
        s1=[]
        for ch in s:
            if ch in '{[(':
                s1.append(ch)
            elif ch in '}])':
                if s1==[]:
                    return False
                if ch =="}":
                    if s1[-1]=='{':
                        del s1[-1]
                    else:
                        return False
                if ch =="]":
                    if s1[-1]=='[':
                        del s1[-1]
                    else:
                        return False
                if ch ==")":
                    if s1[-1]=='(':
                        del s1[-1]
                    else:
                        return False
        if s1 ==[]:
            return True
        else:
            return False