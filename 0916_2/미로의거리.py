from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = []
    for _ in range(N):
        miro.append(list(map(int, list(input()))))
    ans = 0
    sr = None
    sc = None
    for r in range(N):
        for c in range(N):
            if miro[r][c] == 2:
                sr = r
                sc = c
                break
        if sr:
            break
    visited = [[0]*N for _ in range(N)]
    q = deque()
    q.append((sr, sc, 0)) # r, c, 지나온 칸수
    while q:
        nr, nc, t = q.popleft()
        for w in range(4):
            if not ((0<=nr+dr[w]<N) and (0<=nc+dc[w]<N)):
                continue
            if miro[nr+dr[w]][nc+dc[w]] == 1:
                continue
            if visited[nr+dr[w]][nc+dc[w]]:
                continue
            if miro[nr+dr[w]][nc+dc[w]] == 3:
                ans = t
                q.clear()
                break       
            # ans 10000 하는거보다 이렇게하는게 더 안전함. bfs 특성상 목적지를 가장 먼저 발견한 경우가
            # 최단거리일것이기 때문에 이렇게 해도 됨 아니면 bfs자체를 함수로 만들어서 return하는 방법도 있음
            visited[nr][nc] = 1
            q.append((nr+dr[w], nc+dc[w], t+1))
    print(f'#{tc} {ans}')


"""
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
"""