T = int(input())
for tc in range(1, T+1):
    stations = [0]*5000
    N = int(input())
    bus = []
    for _ in range(N):
        bus.append(list(map(int, input().split())))

    P = int(input())
    check = []
    for _ in range(P):
        check.append(int(input()))

    for i in bus:
        for j in range(i[0], i[1]+1):
            stations[j-1] += 1

    ans = []

    for c in check:
        ans.append(stations[c-1])
    dap = ' '.join(map(str, ans))

    print(f'#{tc} {dap}')