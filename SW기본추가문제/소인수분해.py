T = int(input())
for tc in range(1, T+1):
    num = int(input()) # 2^a * 3^b * 5^c * 7^d * 11^e
    factors = [2, 3, 5, 7, 11]
    ans = [0, 0, 0, 0, 0]
    for i, f in enumerate(factors):
        while num % f == 0:
            num = num / f
            ans[i] += 1
    print(f'#{tc} {ans[0]} {ans[1]} {ans[2]} {ans[3]} {ans[4]}')
