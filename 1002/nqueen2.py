def go(now):
    global ans
    if now == N:
        ans += 1
        return

    for i in range(N):
        d1 = i + now
        d2 = i - now + N - 1
        if rvisit[i] or d1visit[d1] or d2visit[d2]:
            continue
        rvisit[i] = True
        d1visit[d1] = True
        d2visit[d2] = True
        go(now + 1)
        rvisit[i] = False
        d1visit[d1] = False
        d2visit[d2] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    rvisit = [False] * N
    d1visit = [False] * (2*N - 1)
    d2visit = [False] * (2*N - 1)
    ans = 0
    # 절반만 탐색
    for i in range(N // 2):
        rvisit[i] = True
        d1visit[i] = True
        d2visit[i + N - 1] = True
        go(1)
        rvisit[i] = False
        d1visit[i] = False
        d2visit[i + N - 1] = False
    # 대칭되는 반대편
    ans *= 2
    # N이 홀수라면 가운데 행은 별도로
    if N % 2:
        i = N // 2
        rvisit[i] = True
        d1visit[i] = True
        d2visit[i + N - 1] = True
        go(1)
        rvisit[i] = False
        d1visit[i] = False
        d2visit[i + N - 1] = False
        
    print(f'#{tc} {ans}')
    