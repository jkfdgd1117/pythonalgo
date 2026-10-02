T = int(input())
for tc in range(1, T+1):
    N = int(input()) 
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    INF = float('inf')
    dp = [INF] * (1 << N)
    dp[0] = 0

    for mask in range(1 << N):
        factory = bin(mask).count('1') # mask.bit_count()
        if factory == N:
            continue
        for i in range(N):
            if mask & (1 << i):
                continue
            next_mask = mask | (1 << i)
            dp[next_mask] = min(
                dp[next_mask],
                dp[mask] + arr[factory][i]
            )
    ans = dp[(1 << N) - 1]
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
