T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    charges = list(map(int, input().split()))
    now = 0
    count = 0
    while now < N:
        able = [c for c in charges if now < c <= now + K]
        if (now + K) >= N:
            now = N
        elif not able:
            count = 0
            break
        elif able:
            now = max(able)
            count += 1
    print(f'#{tc} {count}')