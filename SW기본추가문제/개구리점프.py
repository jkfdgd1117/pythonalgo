T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    pond = list(map(int, input().split()))
    now = 0 
    while now < N:
        leaf = [c for c in range(N) if (now < c <= now + K) and (pond[c] == 1)]
        if leaf:
            now = max(leaf)
        elif (now+K) >= N:
            now = N
        else:
            now += K+1
            break
    print(f'#{tc} {now}')



"""
1
8 3
1 1 0 0 0 0 0 0
"""