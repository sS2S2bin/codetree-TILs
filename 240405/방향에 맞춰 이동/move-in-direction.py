import sys

n = int(input())
arr = [ list(sys.stdin.readline().strip().split()) for _ in range(n) ]
answer = [0,0]

dr = [1,0,-1,0]
dc = [0,-1,0,1]

for direction, count in arr:
    count = int(count)
    if direction == 'E':
        answer[0]+=dr[0]*count
        answer[1]+=dc[0]*count
    elif direction == 'S':
        answer[0]+=dr[1]*count
        answer[1]+=dc[1]*count
    elif direction == 'W':
        answer[0]+=dr[2]*count
        answer[1]+=dc[2]*count
    elif direction == 'N':
        answer[0]+=dr[3]*count
        answer[1]+=dc[3]*count

print(*answer,sep=' ')