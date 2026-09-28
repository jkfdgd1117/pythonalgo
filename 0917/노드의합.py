def go(target):
    global ans
    if target > N:
        return
    if not data[target]:
        data[target*2]
        data[target*2+1]
    else:
        ans += data[target]

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    data = [0]*(N+1)
    for _ in range(M):
        tindex, tdata = map(int, input().split())
        data[tindex] = tdata
    ans = 0
    go(L)
    print(f'#{tc} {ans}')
    




"""
3
5 3 2
4 1
5 2
3 3
10 5 2
8 42
9 468
10 335
6 501
7 170
17 9 4
16 479
17 359
9 963
10 465
11 706
12 146
13 282
14 828
15 962

1
2 3
4 5 6 7
8 9 10 11 12 13 14 15
16 ... 31
32 ... 63
64 ... 127

N = 노드의 갯수
M = 리프노드의 갯수
L = 값을 출력할 목표 노드번호

10 5
10 9 8
7 6 

1. L을 넣으면 L*2, L*2+1 을 불러서 합 구함 (l, r이라고 부름)
2. l,r이 0이면 1로 돌아감
"""