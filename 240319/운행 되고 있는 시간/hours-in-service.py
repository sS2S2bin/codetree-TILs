n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

MAX_NUM = 1000

def calculate(idx):
    time_count = [0] * MAX_NUM
    curr_ans = 0
    for i in range(n):
        if i == idx: continue
        a,b=arr[i][0],arr[i][1]
        for j in range(a,b):
            time_count[j] += 1
    for j in range(1,MAX_NUM):
        if time_count[j] > 0 : curr_ans+=1
    return curr_ans

def solution():
    answer = 0
    for i in range(n):
        answer = max(answer,calculate(i))
    return answer

print(solution())