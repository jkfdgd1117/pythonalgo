dr = [0, 1, 1, 1, 0, -1, -1, -1] # 3 // 4.5 6 7.5 // 9 // 10.5 12 1.5
dc = [1, 1, 0, -1, -1, -1, 0, 1] # 3 4.5 // 6 // 7.5 9 10.5 // 12 // 1.5
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = []
    area.append([10]*(M+2))
    for _ in range(N):
        temp = list(map(int, input().split()))
        temp = [10] + temp + [10]
        area.append(temp)
    area.append([10]*(M+2))
    ans = 0
    for r in range(1, N+1): 
        for c in range(1, M+1):
            validcount = 0
            for i in range(8):
                if area[r][c] > area[r+dr[i]][c+dc[i]]:
                    validcount += 1
            if validcount >= 4:
                ans += 1
    print(f'#{tc} {ans}')