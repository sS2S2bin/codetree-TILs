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
whereman = []
cnt = 1
zerocnt = 0

arr.rotate(1)
whereman.append(0)
arr[0]-=1
if arr[0]==0:
    zerocnt +=1

while(zerocnt<k):
    cnt +=1
    # 회전
    arr.rotate(1)
    for i,idx in enumerate(whereman):
        idx = (idx+1)%(n) #돌아갔으니 사람들 위치도 변경 업데이트
        whereman[i]=idx
        if idx == (n-1): del whereman[i]

    # 앞에 사람이 없고, 0이 아니면 이동
    for i,idx in enumerate(whereman):
        if idx == n-1:
            whereman.pop(i)
        else:
            if (idx+1) not in whereman and arr[idx+1]>0:
                arr[idx+1] -=1
                if arr[idx+1]==0: zerocnt +=1
                if (idx+1)==(n-1): del whereman[i]
                elif(idx+1)!=(n-1): whereman[i]=idx+1

    # 1번에 사람이 없고 안정성 ok 면 사람 추가
    if 0 not in whereman and arr[0]!=0:
        whereman.append(0)
        arr[0] -=1
        if arr[0]==0: zerocnt+=1


print(cnt)