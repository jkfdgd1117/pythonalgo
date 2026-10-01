def subset(idx):
    global ans
    if sum(path) > K:
        return
    if idx == 13:
        if len(path) == N:
            if sum(path) == K:
                ans += 1
        return

    path.append(idx)
    subset(idx + 1)
    path.pop()
    subset(idx + 1)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    path = []
    ans = 0
    subset(1)
    print(f'#{tc} {ans}')
    
    
"""

3
3 6
5 15
5 10

"""