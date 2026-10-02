def start(factory, now_sum):
    global ans

    if now_sum + suffix_min[factory] >= ans:
        return

    if factory == N:
        ans = now_sum
        return

    for i in order[factory]:
        if sel[i]:
            continue

        sel[i] = True
        start(factory + 1, now_sum + arr[factory][i])
        sel[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())    
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    mins = [min(row) for row in arr]
    suffix_min = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        suffix_min[i] = suffix_min[i + 1] + mins[i]
    order = [
        sorted(range(N), key=lambda j: arr[i][j])
        for i in range(N)
    ]
    ans = float('inf')
    sel = [False]*N
    start(0, 0)
    print(f'#{tc} {ans}')



"""

3
3
73 21 21
11 59 40
24 31 83
5
93 4 65 31 66
63 12 60 60 84
87 57 44 35 20
12 9 40 12 40
60 21 3 49 54
6
55 83 32 79 53 70
77 88 80 93 42 29
54 26 5 10 25 94
77 92 82 83 11 51
84 11 21 62 45 58
37 88 13 34 41 4

각 행마다 하나씩 모든 줄에서 고르면 됨 근데 다른곳에서 고른건 못고름

"""
