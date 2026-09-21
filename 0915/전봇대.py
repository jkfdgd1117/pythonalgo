T = int(input())
for tc in range(1, T+1):
    N = int(input())
    suns = []
    ans = 0
    for _ in range(N):
        now = list(map(int, input().split()))
        if suns:
            for sun in suns:
                if (now[0]-sun[0])*(now[1]-sun[1]) < 0:
                    ans += 1
        suns.append(now)
    print(f'#{tc} {ans}')
    


"""
(0, A) (1, B)

A, B를 받았을때

다른 AB들(m,n)이랑 비교했을때
A>m,B<n이나 A<m,B>n인 경우 ans+1
근데이거 전선수가 1000갠데 시간이되나


"""