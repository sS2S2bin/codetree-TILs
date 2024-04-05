import sys
n = int(input())
arr = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def in_range(r,c):
    return 0<=r<n and 0<=c<n

def check_four(r,c):
    threemore = 0
    for i in range(4):
        nr = r+dr[i]
        nc  = c+dc[i]
        if in_range(nr,nc) and arr[nr][nc]==1:
            threemore +=1
    return threemore>2

answer = 0
for r in range(n):
    for c in range(n):
        if check_four(r,c):
            answer+=1

print(answer)