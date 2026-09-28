from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    P = deque(enumerate(map(int, input().split())))
    q = deque()
    ans = 0
    while True:
        if P:
            while len(q) < N:
                q.append(P.popleft())
        now = q.popleft()
        if now[1]//2 != 0:
            now = (now[0], now[1]//2)
            q.append(now)
        if len(q) == 1:
            ans = q.pop()[0]+1
            break
    print(f'#{tc} {ans}')

"""

3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2

"""