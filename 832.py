class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        hi=[]
        for i in image:
            hi.append(i[::-1])
        for r in range(len(hi)):
            for c in range(len(hi[0])):
                if hi[r][c]:
                    hi[r][c]=0
                else:
                    hi[r][c]=1
        return hi

