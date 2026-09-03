T = int(input())

arr = [i for i in range(1, 13)]
N = 12

for tc in range(1, T+1):
    n, k = map(int, input().split())
    ans = 0
    for i in range(1 << N):
        icount = 0
        isum = 0
        for j in range(N):
            if i & (1 << j):
                isum += arr[j]
                icount += 1

        if isum == k and icount == n:
            ans += 1
    print(f'#{tc} {ans}')