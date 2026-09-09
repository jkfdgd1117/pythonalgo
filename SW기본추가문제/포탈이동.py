T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = list(map(int, input().split()))
    visited = [0]*N
    now = 0
    while now != N-1:
        if now == 0:
            visited[0] += 1
            now = 1
            continue
        elif visited[now] == 0:
            visited[now] += 1
            now = rooms[now]-1
            continue
        elif visited[now] != 0:
            visited[now] += 1
            now += 1
            continue
        
    print(f'#{tc} {sum(visited)}')





"""
포탈사용횟수
1 => 2 => 1 => 2 => 3 => 1 => 2 => 3 => 4 => 2 => 3 => 4 => 5
0 => 1 => 2 => 3 => 4 => 5 => 6 => 7 => 8 => 9 => 10 => 11 => 12

방별 포탈사용횟수 = 각방 방문횟수

3
5
0 1 1 2 0
5
0 1 1 1 0
4
0 1 2 0

"""