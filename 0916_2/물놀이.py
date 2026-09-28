from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(input()) for _ in range(N)]
    dist = [[-1] * M for _ in range(N)]
    q = deque()
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 'W':
                dist[r][c] = 0
                q.append((r, c))

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if dist[nr][nc] != -1:
                continue
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

    ans = 0

    for r in range(N):
        for c in range(M):
            if grid[r][c] == 'L':
                ans += dist[r][c]
    print(f'#{tc} {ans}')



"""
6
2 3
WLL
LLL
3 2
WL
LL
LW
4 5
LLLWW
WWLLL
LLLWL
LWLLL
4 5
LLLLL
LLLLL
LLLWL
LLLLL
4 5
LLLWW
LLLWW
LLLWW
LLLWW
5 5
LWLWL
WLWLW
LWLWL
WLWLW
LWLWL
지도는 N*M크기의 격자로 표현이 가능하고, 
위쪽에서 i번째 줄의 왼쪽에서 j번째 칸이 물이면 ‘W’, 땅이면 ‘L’로 표현된다. 
어떤 칸에 사람이 있으면, 
그 칸의 상하좌우에 있는 칸으로 이동하는 것을 반복하여 다른 칸으로 이동할 수 있다. 
단, 격자 밖으로 나가는 이동은 불가능하다. 
땅으로 표현된 모든 칸에 대해서, 어떤 물인 칸으로 이동하기 위한 최소 이동 횟수를 구하고 
모든 이동 횟수의 합을 출력하는 프로그램을 작성하라.

"""