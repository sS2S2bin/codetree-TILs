n,t = list(map(int, input().split()))
r,c,d = list(input().split())

mapping = {'U':0, 'R':1, 'D':2, 'L':3}
dr = [1,0,-1,0]
dc = [0,1,0,-1]
r,c = int(r),int(c)
def in_range(nr,nc):
    return 0<nr<=n and 0<nc<=n

i = mapping[d]
while(t):
    nr = r + dr[i]
    nc = c + dc[i]
    if in_range(nr,nc):
        r,c = nr,nc
    else:
        i = (i+2)%4
        nr,nc = r,c
    t -= 1
print(nr,nc)