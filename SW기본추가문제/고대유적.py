T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = []
    for _ in range(N):
        area.append(list(map(int, input().split())))
    ans = 0
    for r in range(N):
        temp = 1
        for c in range(M-1):
            if area[r][c] == area[r][c+1] == 1:
                temp += 1
                if c == M-2:
                    if ans < temp:
                        ans = temp
                        temp = 1                    
            elif (area[r][c] == 1) and (area[r][c+1] == 0):
                if ans < temp:
                    ans = temp
                    temp = 1
    for c in range(M):
        temp = 1
        for r in range(N-1):
            if area[r][c] == area[r+1][c] == 1:
                temp += 1
                if r == N-2:
                    if ans < temp:
                        ans = temp
                        temp = 1                    
            elif (area[r][c] == 1) and (area[r+1][c] == 0):
                if ans < temp:
                    ans = temp
                    temp = 1
    print(f'#{tc} {ans}')