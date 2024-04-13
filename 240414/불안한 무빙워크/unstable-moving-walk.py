"""
1번에서 탑승 n번에 내림, 이동마다 안정성 -1씩 감소
ㄱ. 무빙워크 회전
ㄴ. 바로 앞 사람없고 안정성>0 이동
ㄷ. 첫 번째 칸에 사람이 없고 안정성 0이 아니면 한명 더
ㄹ. 0이 k개 이상이면 종료

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

    # 앞에 사람이 없고, 0이 아니면 이동
    for idx in range(n-1,0,-1):
        if idx==n-1 and whereman[idx]: 
            whereman[n-1] = False # n번 사람 내려 
        else: 
            whereman[idx] = whereman[idx-1]
        thereisperson = whereman[idx]
        if thereisperson:

            #이동하려는 칸이 맨 마지막 칸이면
            if idx==n-2 and arr[n-1]>0: 
                whereman[n-1]=False
                whereman[idx] = False # 이제 여기 사람 없음
                arr[idx+1] -=1 # 앞 칸 안정성 빼기
                if arr[idx+1]==0: zerocnt +=1
            # 나머지 칸들은 앞에 칸이 0이 아닌지 체크
            elif (not whereman[idx+1]) and arr[idx+1]>0: 
                whereman[idx+1] = True
                whereman[idx] = False # 이제 여기 사람 없음
                arr[idx+1] -=1 # 앞 칸 안정성 빼기
                if arr[idx+1]==0: zerocnt +=1
    whereman[0] = False

    # 1번에 사람이 없고 안정성 ok 면 사람 추가
    if not whereman[0] and arr[0]>0:
        whereman[0] = True
        arr[0] -=1
        if arr[0]==0: zerocnt +=1

print(cnt)