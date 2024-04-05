import sys
direction = list(sys.stdin.readline().strip())
answer = [0,0]
dr = [1,0,-1,0]
dc = [0,1,0,-1]
idx = 3
for dirc in direction:
    if dirc == 'L':
        idx = (idx+3)%4
    elif dirc == 'R':
        idx = (idx+1)%4
    elif dirc == 'F': continue
        answer[0] += dr[idx]
        answer[1] += dc[idx]

print(*answer,sep=' ')