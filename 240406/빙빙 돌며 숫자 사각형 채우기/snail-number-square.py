n,m = list(map(int,input().split()))
arr = [[0]*m for _ in range(n)]

dr = [0,1,0,-1] # 오, 아래, 왼, 위
dc = [1,0,-1,0]
r,c = 0,0
direction = 0
arr[r][c] = 1

def in_range(nr,nc):
    return 0<=nr<n and 0<=nc<m

for i in range(2,n*m+1): # 1일떄 확인해야함
    nr = r+dr[direction]
    nc = c+dc[direction]
    if not in_range(nr,nc) or arr[nr][nc]!=0:
        direction = (direction+1)%4
        nr = r+dr[direction]
        nc = c+dc[direction]
    arr[nr][nc] = i
    r,c = nr,nc

for rows in arr:
    print(*rows,sep=' ')