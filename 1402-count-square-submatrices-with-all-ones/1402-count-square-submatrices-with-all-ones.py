class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n,m=len(matrix),len(matrix[0])
        psum=[[0]*m for _ in range(n)]
        psum[0][0]=matrix[0][0]
        for i in range(n):
            for j in range(m):
                psum[i][j]=matrix[i][j]
                if i>0:
                    psum[i][j]+=psum[i-1][j]
                if j>0:
                    psum[i][j]+=psum[i][j-1]
                if i>0 and j>0:
                    psum[i][j]-=psum[i-1][j-1]
        # print(psum)
        ans=0
        mini=min(n,m)
        for k in range(1,mini+1):
            for r1 in range(0,n-k+1):
                for c1 in range(0,m-k+1):
                    r2,c2=r1+k-1,c1+k-1
                    tempsum=psum[r2][c2]
                    if r1>0:
                        tempsum-=psum[r1-1][c2]
                    if c1>0:
                        tempsum-=psum[r2][c1-1]
                    if r1>0 and c1>0:
                        tempsum+=psum[r1-1][c1-1]
                    if tempsum==k*k:
                        ans+=1
        return ans