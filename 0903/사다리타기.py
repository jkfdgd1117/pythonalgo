dr = [0, 0, -1]
dc = [1, -1, 0]     # 우 좌 상
for _ in range(10):
    T = int(input())
    ladder = []
    for _ in range(100):
        temp = list(map(int, input().split()))
        temp = [0] + temp + [0]
        ladder.append(temp)

    now = [99, ladder[99].index(2)]
    while now[0] > 0:
        for i in range(3):
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]

            if ladder[nr][nc] == 1:
                ladder[now[0]][now[1]] = 0 # 지나간 길 끊기
                now = [nr, nc]
                break
    print(f'#{T} {now[1]-1}')
