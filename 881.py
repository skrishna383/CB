class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans=0
        l=0
        r=len(people)-1
        while l<=r:
            w=people[l]+people[r]
            if w>limit:
                ans=ans+1
                r=r-1
            else:
                ans=ans+1
                r=r-1
                l=l+1
        return ans

                    
            


