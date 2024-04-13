"""
1번에서 n번에 내림, 안정성 -1씩 감소, 안정성 0이면 못올라감
ㄱ. 무빙워크 회전
ㄴ. 안정성 0 아니면 이동
ㄷ. 첫 번째 칸에 사람이 없고 안정성 0이 아니면 한명 더(한 번에 한 사람??)
ㄹ. 0이 k개 이상이면 종료

1. 아이디어
2. 시간복잡도
3. 자료구조
"""
from collections import deque
n,k = list(map(int, input().split()))
arr = deque(map(int, input().split()))
whereman = [False]*n
cnt = 1
zerocnt = 0

arr.rotate(1)
whereman[0]=True
arr[0]-=1
if arr[0]==0:
    zerocnt +=1

while(zerocnt<k):
    cnt +=1
    # 회전
    arr.rotate(1)
    for i in range(n-1,0,-1):
        if i==n-1 and whereman[i]: 
            whereman[n-1] = False
        else: 
            whereman[i] = whereman[i-1]
    whereman[0] = False

    # 앞에 사람이 없고, 0이 아니면 이동
    for idx,thereisperson in enumerate(whereman):
        if thereisperson:
            if (idx+1)<n and (not whereman[idx+1]) and arr[idx+1]>0:
                whereman[idx] = False # 이제 여기 사람 없음
                arr[idx+1] -=1 # 앞 칸 안정성 빼기
                if arr[idx+1]==0: 
                    zerocnt +=1
                if (idx+1)==(n-1): 
                    whereman[n-1] = False #사람 내림
                elif(idx+1)!=(n-1): 
                    whereman[idx+1] = True

    # 1번에 사람이 없고 안정성 ok 면 사람 추가
    if not whereman[0] and arr[0]>0:
        whereman[0] = True
        arr[0] -=1
        if arr[0]==0:
            zerocnt +=1

# print("answer : {}, zero cnt : {}, k:{} , arr:{}".format(cnt,zerocnt,k,arr))

print(cnt)