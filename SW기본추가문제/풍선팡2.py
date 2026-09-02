T = int(input())

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    maxf = 0
    for r in range(N):
        for c in range(M):
            f = grid[r][c]
            localsum = f

            for d in range(4):
                nr = r + di[d] 
                nc = c + dj[d] 

                if (0 <= nr < N) and (0 <= nc < M):
                    localsum += grid[nr][nc]

            maxf = max(maxf, localsum)

    print(f'#{tc} {maxf}')