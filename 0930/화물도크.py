T = int(input())
for tc in range(1, T+1):
    N = int(input())
    reqs = []
    for _ in range(N):
        reqs.append(list(map(int, input().split())))
    reqs.sort(key=lambda x:x[1])
    now = 0     # 마지막 작업 종료시간(초기값 0)
    ans = 0
    for r in reqs:
        if r[0] >= now:
            now = r[1]
            ans += 1
    print(f'#{tc} {ans}')



"""
3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24
"""