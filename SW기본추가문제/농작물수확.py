T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    mid = N // 2
    bat = []
    for i in range(N):
        bat.append(list(input()))
    sum = 0
    for r in range(N):
        for c in range(N):
           if (abs(c-mid) + abs(r-mid) <= mid):
               sum += int(bat[r][c])
    print(f'#{test_case} {sum}')