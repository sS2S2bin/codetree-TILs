"""
0. 해결 필요
- 팀장 : 1(필수), 팀원 : n
- 검사자 수 최솟값 구하는 프로그램 >> 구현?그리디?
1. 아이디어
팀장 
2. 시간복잡도
3. 자료구조
"""
import sys
n = int(input())
customercount = list(map(int,sys.stdin.readline().rstrip().split()))
captin, notcaptin = list(map(int,sys.stdin.readline().rstrip().split()))
answer = 0

for i in range(n):
    # captin 1명 배정
    answer +=1
    if customercount[i]>captin:
        customercount[i] -= captin
        # print('after captin',customercount[i])
        if customercount[i]>notcaptin:
            # print(round(customercount[i]/notcaptin))
            answer += round(customercount[i]/notcaptin)
        else:
            answer +=1
    else: continue

print(answer)