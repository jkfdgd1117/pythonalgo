T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    target = max(trees)
    total = 0
    odd = 0
    
    for t in trees:
        diff = target - t
        total += diff
        odd += diff % 2
    ans = 0
    
    while True:
        odd_days = (ans + 1) // 2
        even_days = ans // 2
        if odd_days >= odd:
            remain = total - odd
            extra_odd = (odd_days - odd) // 2
            if even_days + extra_odd >= remain // 2:
                break
        ans += 1

    print(f'#{tc} {ans}')
        

"""
11
2
5 5
2
4 2
2
3 4
4
2 3 10 5
4
1 2 3 4
20
26 19 23 2 24 2 17 15 1 27 6 29 18 23 27 13 26 21 9 1
20
4 5 3 4 2 4 4 3 5 2 2 3 5 5 5 2 5 2 5 5
20
1 3 6 5 5 1 5 4 3 5 4 2 4 6 5 5 4 5 5 3
20
4 5 6 6 5 3 1 3 3 3 3 5 3 3 3 4 5 1 4 3
20
26 6 8 15 10 15 14 6 19 16 5 13 9 12 14 29 28 3 12 27
30
3 2 5 5 5 4 4 5 2 4 3 4 3 5 5 2 5 4 2 5 2 1 5 4 4 3 2 4 2 4

1
30
3 2 5 5 5 4 4 5 2 4 3 4 3 5 5 2 5 4 2 5 2 1 5 4 4 3 2 4 2 4
"""
