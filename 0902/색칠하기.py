T = int(input())
for tc in range(1, T+1):
    grid = [[1]*10 for _ in range(10)]
    N = int(input())
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        color += 1
        for r in range(r1, r2 +1):
            for c in range(c1, c2 +1):
                grid[r][c] = grid[r][c]*color
    counts = 0
    for r in grid:
        for c in r:
            if c % 6 == 0:
                counts += 1
    print(f'#{tc} {counts}')