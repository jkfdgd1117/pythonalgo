T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pad = list(map(int, input()))
    M = int(input())
    code = list(map(int, input()))
    for c in pad:
        if code and code[0] == c:
            del code[0]
    if code:
        ans = 0
    else:
        ans = 1
    print(f'#{tc} {ans}')