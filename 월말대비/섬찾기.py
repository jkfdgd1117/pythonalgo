dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def go(r, c):
    global grid
    if grid[r][c] == 'W':
        return
    else:
        grid[r][c] = 'W'
        for i in range(4):
            if (0<=(r+dr[i])<N) and (0<=(c+dc[i])<M):
                go(r+dr[i], c+dc[i])
        return True
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(input()))
    ans = 0
    for r in range(N):
        for c in range(M):
            if go(r, c):
                ans += 1
    print(f'#{tc} {ans}')


"""
3
5 5
WWWWW
WLLWW
WLWWW
WWLWW
WWLLW
5 7
LLLLLLL
LLLLLLL
LLLLLLL
LLLLLLL
LLLLLLL
6 6
LWLWLW
WLWLWL
LWLWLW
WLWLWL
LWLWLW
WLWLWL
"""