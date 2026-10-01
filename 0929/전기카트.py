def go(d, now, hap):
    global ans
    if hap > ans:
        return
    if d == N-1:
        if ans > hap+arr[now][0]:
            ans = hap+arr[now][0]
        return
    for i in range(1, N): # i = 다음으로 이동할 구역 번호
        if visited[i]:
            continue
        visited[i] = True
        go(d+1, i, hap+arr[now][i])
        visited[i] = False
        

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _  in range(N):
        arr.append(list(map(int, input().split())))
    ans = float('inf')
    visited = [False]*N
    go(0, 0, 0)
    print(f'#{tc} {ans}')

"""
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0

골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.

두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

문제에선 1번이 사무실, 2번부터 관리구역이라 했는데, 편리를 위해서
0번을 사무실, 1번부터 관리구역으로 두고 풀거임

1 -> 2 가는 경로의 비용은 arr[1][2]

누적 경로비용을 인자로 넘기면 좋을거같음(가지치기, 재귀 용이)

visited는 필요함 근데 path는? 필요없을거같음

재귀함수에서 할일은? visited 갱신하고 누적합에 경로비용 추가

근데 path가 없으니 depth가 있어야함(기저조건 위해서)

1~N-1의 순열로 구역을 방문해야함. 어디에서 어디로 가는지 알아야하므로 지금 위치한 구역 번호정도는 인자로 넘겨줘야할거임

마지막 방문은 따로 처리할거니 뎁스 N-1에서 끊음

중간에 ans보다 커지는 경우 가지치기
"""
