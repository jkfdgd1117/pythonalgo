def go(w, num):
    global ans
    if len(path) == num:
        ans += 1
        return
    if not hubos[w]:
        return
    for x in hubos[w]:
        valid = True
        for prev_w in range(w):
            prev_i = path[prev_w]
            if x == prev_i:
                valid = False
                break
            if abs(x - prev_i) == abs(w - prev_w):
                valid = False
                break
        if valid:   
            path.append(x)
            go(w+1, num)
            path.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    hubos = [[i for i in range(N)] for _ in range(N)]
    path = []
    ans = 0
    go(0, N)
    print(f'#{tc} {ans}')

"""
0~N-1까지의 숫자를 1차원 배열에 넣음(열마다 몇번째 행에 퀸 놓는지)
[0, 0, ... 0, 0]
i 넣으면 다음칸부터 i-1, i-2... 와 i와 i+1, i+2 ...가 금지숫자
2i-j
첫 칸에 0~ N-1 넣으면서 경우의 수 탐색
j번칸에 숫자 채운다음 그 이후칸들 금지숫자 갱신
마지막칸 도착 안했는데 가능한숫자 None이면 폐기
다찾으면 경우의수 +1

"""