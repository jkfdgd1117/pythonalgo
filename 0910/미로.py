dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def go(r, c):
    global found
    if miro[r][c] == 3:
        found = 1
        return
    elif miro[r][c] == 1:
        return
    else:
        miro[r][c] = 1
        for i in range(4):
            go(r+dr[i], c+dc[i])
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = []
    miro.append([1]*(N+2))
    for r in range(N):
        temp = list(map(int, list(input())))
        for c, j in enumerate(temp):
            if j == 2:
                nowr = r+1
                nowc = c+1
        temp = [1]+temp+[1]
        miro.append(temp)
    miro.append([1]*(N+2))
    found = 0
    
    go(nowr, nowc)
    print(f'#{tc} {found}')