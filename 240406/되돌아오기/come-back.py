n = int(input())
arr = [list(input().split()) for _ in range(n)]

def solution():
    mapping = {'N':0 , 'E':1 , 'S':2 , 'W':3 }

    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    r,c= 0,0
    t = 0
    for i in range(n):
        direction = mapping[arr[i][0]]
        for ii in range(int(arr[i][1])):
            t +=1
            r += dr[direction]
            c += dc[direction]
            if r==0 and c==0:
                return print(t)
    return print(-1)

solution()