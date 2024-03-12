N = int(input())
checkpointList = [list(map(int,input().split())) for _ in range(N)]
checkidxList = [ i for i in range(N)]
# print(N,checkpointList)
answer = 10000000
lenN = len(checkpointList)

def calculate(checkidxList):
    shrtestcut = 0
    for i in range(len(checkidxList)-1):
        idxN = checkidxList[i]
        idxNext = checkidxList[i+1]
        # print(idxN,idxNext)
        x1,y1 = checkpointList[idxN][0], checkpointList[idxN][1]
        x2,y2 = checkpointList[idxNext][0], checkpointList[idxNext][1]
        # print(x1,x2,'\t', y1,y2)
        shrtestcut = shrtestcut + abs(x1-x2) + abs(y1-y2)
        # print('shrt:',shrtestcut)
    return shrtestcut

def jumpsecret():
    global answer
    for i in range(1,lenN-1):
        checkidxList.pop(i)
        # print("check list -> ",checkidxList)
        answer = min(answer, calculate(checkidxList))
        # print(answer)
        checkidxList.insert(i,i)
    return print(answer)
jumpsecret()