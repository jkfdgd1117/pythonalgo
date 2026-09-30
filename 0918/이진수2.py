T = int(input())
for tc in range(1, T+1):
    N = float(input())
    ans = ''
    for i in range(1, 14):
        if i == 13:
            ans = 'overflow'
            break
        sub = 1/(2**i)
        if N - sub == 0:
            ans += '1'
            break
        if N - sub > 0:
            N -= sub
            ans += '1'
            continue
        if N - sub < 0:
            ans += '0'
            continue
    print(f'#{tc} {ans}')


"""
i = 1부터 13까지
N에서 1/(2**i)을 빼본다
음수 안되면 빼고 i+1로 넘어감, ans += '1'
만약 음수되면 안빼고 i+1으로 넘어감, ans += '0'
만약 0 되면 그대로 종료하고 ans 출력하면됨
만약 i == 13 되면 그대로 종료하고 overflow 출력하면됨

3
0.625
0.1
0.125

"""
