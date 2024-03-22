# 아이디어
# 1~2*N의 최대 숫자가 주어졌을 때
# b 하나씩 꺼내서 해당 숫자보다 1큰 숫자가 b에 들어있는지 파악
# 숫자가 있으면 노카운트
# 숫자가 없으면 카운트

# 시간 복잡도
# b순회하는거만 O(N)

# 자료구조
# 

n = int(input())
b_arr =[
    int(input())
    for _ in range(n)
]

MAX_NUM = 2*n
answer = 0
for b in b_arr:
    if (b+1) not in b_arr and b+1<=MAX_NUM:
        answer +=1
print(answer)