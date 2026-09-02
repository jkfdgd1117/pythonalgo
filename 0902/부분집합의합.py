def makesubset(i):
    if i == M+1:
        allsets.append(path[:])
        return
    path.append(i)
    makesubset(i+1)
    path.pop()
    makesubset(i+1)
M = 12


allsets = []
path = []
makesubset(1)
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0
    for c in allsets:
        if len(c) == N:
            if sum(c) == K:
                ans += 1
    print(f'#{tc} {ans}')


# T = int(input())
# for tc in range(1, T+1):
#     path = []