T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    mid = int(N/2)
    bat = []
    for i in range(N):
        bat += input().split()
    sum = 0
    for y in range(N):
        for x in range(N):
           if (abs(x-mid) + abs(y-mid) <= mid):
               sum += int(bat[y][x])
    print(f'#{test_case} {sum}')