nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for _ in range(10):
    tc, N = input().split()
    N = int(N)
    arr = list(input().split())
    counts = [0]*10
    for num in arr:
        counts[nums.index(num)] += 1
    ans = ''
    for i in range(10):
        for _ in range(counts[i]):
            ans += nums[i]
            ans += ' '
    print(f'{tc} {ans}')