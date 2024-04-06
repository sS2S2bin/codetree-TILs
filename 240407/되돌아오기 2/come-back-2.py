arr = list(input())

def solution():
    direction = 0
    r,c = 0,0
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    t = 0
    for dir in arr:
        t += 1
        if dir == 'L':
            direction = (direction+3)%4
        elif dir == 'R':
            direction = (direction+1)%4
        else :
            r,c = r+dr[direction], c+dc[direction]
        if r==0 and c==0:
            return print(t)
    return print(-1)
solution()