T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    ans = 0
    trucks.sort(reverse=True)
    weights.sort(reverse=True)
    for t in trucks:
        now = 0
        for w in weights:
            if t-w >= 0 :
                now = w
                weights.remove(w)
                break
        ans += now
    print(f'#{tc} {ans}')

"""

3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13

"""