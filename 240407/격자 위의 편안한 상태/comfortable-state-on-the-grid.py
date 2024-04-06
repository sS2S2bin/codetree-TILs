import sys
n,m = list(map(int, input().split()))
arr = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
visited = [[False]*(n+1) for _ in range(n+1)]

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def in_range(nr,nc):
    return 1<=nr<=n and 1<=nc<=n

def four_check(r,c):
    cnt = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if in_range(nr,nc) and visited[nr][nc]==True:
            cnt+=1
    return cnt==3

for r,c in arr:
    visited[r][c] = True
    if four_check(r,c):
        print(1)
    else:
        print(0)