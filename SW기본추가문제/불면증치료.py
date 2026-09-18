T = int(input())
for tc in range(1, T+1):
    N = input()
    seen = set()
    for c in N:
        seen.add(c)
    i = 2
    while len(seen) < 10:
        x = int(N)*i
        for c in str(x):
            seen.add(c)
        i += 1
    print(f'#{tc} {x}')

"""
5
1
2
11
1295
1692

"""