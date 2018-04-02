a = [1,2,3,4,2,5,3,1,1,2]
target_sum = 5

start_idx = 0
end_idx = 0
curr_sum = 0
cnt = 0

while True:
    print('start_idx=', start_idx, ', end_idx=', end_idx)
    if curr_sum == target_sum:
        print('Gotcha!')
        cnt += 1
        start_idx += 1
    elif end_idx == len(a) - 1 and curr_sum < target_sum:
        break
    elif start_idx == end_idx or curr_sum < target_sum:
        end_idx+=1
    elif curr_sum > target_sum:
        start_idx+=1

    print('-------------------------------------------------')
    print('current range=', a[start_idx:end_idx])
    print('current sum=', curr_sum)

    curr_sum = sum(a[start_idx:end_idx])


print('COUNT=', cnt)


