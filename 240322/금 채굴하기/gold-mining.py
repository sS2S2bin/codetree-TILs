n,m = map(int,input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

answer = 0
# 왼쪽 아래 대각선 / 오른쪽 아래 대각선 / 오른쪽 위로 대각선 / 왼쪽 위로 대각선
sider = [1,1,-1,-1]
sidec = [-1,1,1,-1]
def sidebfs(a,b,k):
    curr_cnt = 0
    curr_cnt += arr[a][b] # k = 0 일때
        # k = 1일때 ~ k+1일때까지
    for k in range(1,k+1):
        na,nb = a-k, b # 중심점으로 부터 맨 위에 좌표 구하기
        for i in range(4):
            # k번 내려가고 올라가기
            for _ in range(k):
                if 0<=na<n and 0<=nb<n and arr[na][nb]==1:
                    curr_cnt +=1
                na = sider[i] + na
                nb = sidec[i] + nb
    return curr_cnt

def solution():
    # 마름모 중심
    global answer
    for a in range(n):
        for b in range(n):
            # k 0부터
            for k in range(n+1):
                cost = pow(k,2)+pow(k+1,2)
                # 가장자리 체크하고 금 갯수 리턴
                curr_cnt = sidebfs(a,b,k)
                # print("k:",k, curr_cnt)
                if curr_cnt*m>=cost:
                    answer = max(curr_cnt, answer)
    print(answer)
    return answer

"""
# sol1
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
            for k in range(n+1):
                cost = pow(k,2)+pow(k+1,2)
                curr_money, curr_cnt = bfs(a,b,k)
                if curr_money>=cost:
                    answer = max(curr_cnt,answer)
    print(answer)
    return answer
"""

solution()