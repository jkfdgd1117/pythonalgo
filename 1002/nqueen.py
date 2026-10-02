def go(now):    # now는 현재 놓은 퀸의 수 = 지금 몇열에 퀸 놓는중인지
    global ans
    if now == N:
        ans += 1
        return
    
    for i in range(N):  # now열 i번째 행에 퀸 놓을까말까 고민중
        if rvisit[i] or d1visit[abs(i+now)] or d2visit[abs(i-now+N-1)]:
            continue
        rvisit[i] = True
        d1visit[abs(i+now)] = True
        d2visit[abs(i-now+N-1)] = True
        go(now+1)
        rvisit[i] = False
        d1visit[abs(i+now)] = False
        d2visit[abs(i-now+N-1)] = False
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rvisit = [False]*N
    d1visit = [False]*(N*2-1)
    d2visit = [False]*(N*2-1)
    ans = 0
    go(0)
    print(f'#{tc} {ans}')


"""
2
1
2

매번 놓을때마다
visited를 갱신하는데
어떻게 갱신하느냐?
visited를 행, 우상대각선, 우하대각선을 세개를 만들어서 따로 갱신해야함
그리고 그중 하나라도 True면 못놓는곳임

대각선 visited는 어떻게 만드느냐
대각선 한줄마다 번호를 붙이면
2N-1개가 생김

근데 지금 놓는칸 보고 무슨대각선 쏘는지 어떻게아느냐?

j번째열 i번째 행에 놨다 > abs(i-j)가 일정한애들이 같은 대각선에 있는애들임

그러면 rvisit[i] = True
또 우상대각선 d1visit[abs(i-j)] = True
우하대각선 d2visit[abs(i+j)] = True



"""
