
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = []
    area += [[1]*(N+2)]
    for _ in range(N):
        temp = list(map(int, input().split()))
        temp = [1] + temp + [1]
        area.append(temp)
    area += [[1]*(N+2)]
    safe = 0
    ar = 0
    ac = 0
    for r in range(N+2):
        for c in range(N+2):
            if area[r][c] == 0:
                safe += 1
            elif area[r][c] == 2:
                ar = r
                ac = c
    for i in range(4):
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        w = 1
        while area[ar+w*dr[i]][ac+w*dc[i]] != 1:
            safe -= 1
            w += 1
    print(f'#{tc} {safe}')