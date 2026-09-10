def go(start):
    global ans
    if start == 99:
        ans = 1
    visited[start] = 1
    if jido[start]:
        for j in jido[start]:
            go(j)
    
for _ in range(10):
    tc, N = map(int, input().split())
    jido = [[] for _ in range(100)]
    visited = [0]*100
    temp = list(map(int, input().split()))
    for i in range(0, N*2, 2):
        jido[temp[i]].append(temp[i+1])
    ans = 0
    go(0)
    print(f'#{tc} {ans}')