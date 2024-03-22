"""
1. 아이디어
for r
    for c
        1 이고 방문 안했던 곳이면 dfs(r,c) 
        result_arr = dfs(,)결과값 append 
len(result_arr)
println(result_arr 원소 1개씩)

dfs 
if 0을 이거나 배열 밖으로 넘어가면 
    멈추고 다른 방향
else if 배열 이내의 + 1이면 
    방문 한 곳은 check
    cnt += 1
    dr,dy 로 한 방향으로만 쭉 간다 dfs() 재귀

    
2. 시간복잡도
DFS O(V+E)
2중 for O(n^4)

3. 자료구조
결과값 list 
"""

n = int(input())
arr =[list(map(int, input().split())) for _ in range(n)]
check_arr = [ [False]*n for _ in range(n) ]
result_arr = []

# 오 하 왼 상
dr = [0,1,0,-1]
dc = [1,0,-1,0]
cnt = 0

def dfs(r,c):
    global cnt
    cnt+=1
    for i in range(4):
        nr = r+ dr[i]
        nc = c+ dc[i]
        if 0<=nr<n and 0<=nc<n:
            if check_arr[nr][nc]==False and arr[nr][nc]==1:
                check_arr[nr][nc] = True
                dfs(nr,nc)

for r in range(n):
    for c in range(n):
        if arr[r][c]==1 and check_arr[r][c]==False:
            check_arr[r][c]=True
            cnt = 0
            dfs(r,c)
            result_arr.append(cnt)
            
result_arr.sort()            
print(len(result_arr))
for i in result_arr:
    print(i)