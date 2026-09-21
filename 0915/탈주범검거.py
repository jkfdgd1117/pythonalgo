dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

pipe = [[],
    [0, 1, 2, 3],  # 1: 우 하 좌 상
    [1, 3],        # 2: 하 상
    [0, 2],        # 3: 우 좌
    [0, 3],        # 4: 우 상
    [0, 1],        # 5: 하 우
    [1, 2],        # 6: 하 좌
    [2, 3]         # 7: 상 좌
]

def go(r, c, t):
    global pos, ans
    if t == L-1:
        return
    for d in pipe[grid[r][c]]:
        nr = r+dr[d]
        nc = c+dc[d]

        if not (0 <= nr < N and 0 <= nc < M):
            continue
        if pos[nr][nc]:
            continue
        if grid[nr][nc] == 0:
            continue
        if (d+2) % 4 not in pipe[grid[nr][nc]]:
            continue
        pos[nr][nc] = 1
        ans += 1
        go(nr, nc, t+1)

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    ans = 1
    pos = [[0]*M for _ in range(N)]
    pos[R][C] = 1
    go(R, C, 0)
    print(f'#{tc} {ans}')


"""
1 : 상하좌우
- 상/하/좌/우 방향에 이동할 수 있는 터널 있는지 확인 
2 : 상하
- 상/하 방향에 이동할 수 있는 터널 있는지 확인
3 : 좌우
4 : 상우
5 : 하우
6 : 하좌
7 : 상좌

상으로 이동할경우
- 상방향에 터널이 하 있는 터널인지 확인해야함
- 1, 2, 5, 6 인지 확인
우로 이동할경우
- 우방향 터널이 좌 있는지 확인
- 1, 3, 6, 7 인지 확인
하로 이동할경우
- 하방향 터널이 상 있는지 확인
- 1, 2, 4, 7
좌로 이동할경우
- 좌방향 터널이 우 있는지 확인
- 1, 3, 4, 5


"""