k,n = list(map(int, input().split()))

each = []
def backtracking(each):
    if len(each)==n:
        print(*each, sep=' ')
        return 
    for i in range(1, k+1):
        each.append(i)
        backtracking(each)
        each.pop()
    return

backtracking(each)