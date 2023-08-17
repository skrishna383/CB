class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        for i in range(1, n):
            triangle[i][0] += triangle[i - 1][0]
            triangle[i][-1] += triangle[i - 1][-1]
        for i in range(1, n):
            for j in range(1,i):
                triangle[i][j] += min(triangle[i - 1][j], triangle[i-1][j -1])
        print(triangle)
        return min(triangle[-1])