n,m = map(int,input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

answer = 0
def bfs(a,b,k):
    curr_cnt = 0
    curr_money = 0
    for r in range(n):
        for c in range(n):
            if abs(r-a)+abs(b-c) <=k and arr[r][c]==1:
                curr_cnt +=1
    curr_money=curr_cnt*m
    return curr_money, curr_cnt


def solution():
    global answer
    # a,b 중심점이 0,0 일때 
    for a in range(n):
        for b in range(n):
            # k 가 0,1,2.. n일때까지 구함
            for k in range(n):
                cost = pow(k,2)+pow(k+1,2)
                curr_money, curr_cnt = bfs(a,b,k)
                if curr_money>=cost:
                    answer = max(curr_cnt,answer)
    print(answer)
    return answer

solution()