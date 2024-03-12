import sys
ans = sys.maxsize
n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

    
def solution():
    global ans
    ar = []
    for i in range(len(arr)):
        ar += arr[i+1:]
        ar += arr[0:i]
        # print('{} 번째 리스트는 {}'.format(i,ar))
        curr_ans = 0
        for idx,value in enumerate(ar):
            curr_ans += value*(idx+1)
            # print('cur_ans {} += value{} * idx{}'.format(curr_ans, value, idx+1))
        # print('curr ->',curr_ans,'ans ->',ans)
        ans = min(curr_ans, ans)
        ar = []
    return ans

print(solution())