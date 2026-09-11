def make(i, sel, hap):
    global ans
    if hap > ans:
        return
    if i == N:
        if ans > hap:
            ans = hap
        return
    for j in range(N):
        if not sel[j]:
            sel[j] = 1
            make(i+1, sel, hap+matrix[i][j])
            sel[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = 100
    lsel = [0]*N
    make(0, lsel, 0)
    print(f'#{tc} {ans}')