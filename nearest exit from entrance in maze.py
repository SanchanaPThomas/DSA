class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n=len(maze),len(maze[0])
        sr,sc=entrance

        dirs=[(-1,0),(1,0),(0,-1),(0,1)]
        q=deque()
        q.append((sr,sc,0))
        maze[sr][sc]='+'
        while q:
            r,c,dist=q.popleft()
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                if not (0<=nr<m and 0<=nc<n):
                    continue
                if maze[nr][nc]=="+":
                    continue
                if nr==0 or nr==m-1 or nc==0 or nc==n-1:
                    return dist+1
                maze[nr][nc]='+'
                q.append((nr,nc,dist+1))
        return -1
