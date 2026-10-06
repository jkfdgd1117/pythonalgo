def comb(start, now):
    global ans

    if now == N // 2:
        A = 0
        B = 0
        for i in range(N):
            for j in range(i + 1, N):
                if selected[i] and selected[j]:
                    A += table[i][j] + table[j][i]
                elif not selected[i] and not selected[j]:
                    B += table[i][j] + table[j][i]
        ans = min(ans, abs(A - B))
        return
    for i in range(start, N):
        selected[i] = True
        comb(i + 1, now + 1)
        selected[i] = False   

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    selected = [False]*N
    selected[0] = True
    comb(1, 1)
    print(f'#{tc} {ans}')
    





"""
4
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0
4
0 7 1 1
7 0 6 2
1 1 0 2
10 1 9 0
6
0 37 26 52 77 20
32 0 15 26 75 16
54 33 0 79 37 90
92 10 66 0 92 3
64 7 89 89 0 21
80 49 94 68 5 0
6
0 73 30 81 27 94
98 0 91 9 97 24
51 100 0 35 41 98
26 26 96 0 26 90
73 37 39 57 0 16
90 88 97 9 95 0

N = [4, 6, 8, 10, 12, 14, 16]
식재료 N개 있으면 (N은 짝수, 4<=N<=16) 
N/2개씩 써서 요리 A, B를 만들어야함

123 456 인 경우
12 13 23 21 31 32 의 합
45 46 56 54 64 65 의 합
의 차가 케이스 하나가 되고
결론적으로 최소화되는 케이스를 찾아야함

123 456
124 356
125 346
126 345
134 256
135 246
136 245
423 156 (156 423)
523 146 (146 523)
623 145 (145 623)

6*5*4/6 20개의 경우 있는데 A랑 B랑 순서도 상관없으니 /2 하면 10개있을거같음
comb(N, N/2)/2개의 경우의 수 있을거임
최대 16*15*14*13*12*11*10*9/2개 ~> 약 2.6억개 

/2를 어떻게하느냐? A요리에 1을 뽑는 경우/안뽑는경우 로 나누면 됨

뽑았다면? 가능한 시너지 조합별로 table[r][c]와 table[N-r-1][N-c-1]의 차의 합를 구하면 될거같음

가능한 시너지 조합 만드는건? 순열

넘겨줘야할 인자는 차의 누적합 chas, 재료 몇개 썼는지 now 두개일듯?



"""
