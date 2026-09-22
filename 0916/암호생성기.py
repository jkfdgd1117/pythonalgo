from collections import deque

for tc in range(1, 11):
    T = int(input())
    q = deque(map(int, input().split()))
    while True:
        for i in range(1, 6):
            temp = q.popleft()-i
            if temp <= 0:
                temp = 0 
                q.append(temp)
                break
            q.append(temp)
        if q[-1] == 0:
            break
    print(f'#{tc}', *q)