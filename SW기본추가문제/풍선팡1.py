T = int(input())
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    maxf = 0
    for r in range(N):
        for c in range(M):
            f = grid[r][c]
            localsum = f
            for i in range(1,f+1): 
                if r-i >= 0:
                    localsum += grid[r-i][c]
                if r+i <= N-1:
                    localsum += grid[r+i][c]
                if c-i >= 0:
                    localsum += grid[r][c-i]
                if c+i <= M-1:
                    localsum += grid[r][c+i]
            if maxf <= localsum:
                maxf = localsum
    print(f'#{tc} {maxf}')