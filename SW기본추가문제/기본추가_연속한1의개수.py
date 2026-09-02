T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    record = 0
    streak = 0
    for i in range(N):
        if arr[i] == 1:
            streak += 1
            if record <= streak:
                record = streak
        else:
            streak = 0
    print(f'#{tc} {record}')