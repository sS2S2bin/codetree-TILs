n,m = map(int,input().split())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))
b_set = set(b_arr)
b_cnt_dict = {}

for i,b in enumerate(b_arr):
    b_cnt_dict[b] = b_arr.count(b)

continue_cnt_value = 0
answer = 0 
prev_bool = False
for i in range(n-m+1):
    continue_cnt_value = 0
    for b in b_set:
        if a_arr[i:i+m].count(b)==b_cnt_dict[b]:
            # print(a_arr[i:i+m],'{},a cnt : {}, b cnt : {}'.format(b,a_arr[i:i+m].count(b),b_cnt_dict[b]))
            # print()
            continue_cnt_value += a_arr[i:i+m].count(b)
            prev_bool = True
        # else: 
        #     continue_cnt_value = 0
        #     prev_bool = False
    # if not prev_bool : 
    #     continue_cnt_value = 0
    if continue_cnt_value == m:
        answer += 1
        continue_cnt_value = 0
        prev_bool = False

print(answer)