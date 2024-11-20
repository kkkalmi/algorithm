while True:
    cnt = 0
    nums = list(map(int, input().split()))
    if -1 in nums:
        break
    for n in nums[:len(nums)-1]:
        if n * 2 in nums:
            cnt += 1
    print(cnt)