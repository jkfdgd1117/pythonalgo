def go(start):
    visited[start] = 1
    for way in nodes[start]:
        if visited[way] == 0:
            go(way)
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    nodes = [[] for _ in range(V+1)]
    for _ in range(E):
        fr, to = map(int, input().split())
        nodes[fr].append(to)
    S, G = map(int, input().split())
    visited = [0]*(V+1)
    go(S)
    if visited[G]:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')


"""

1
6 5
1 4
1 3
2 3
2 5
4 6
1 6

7 4
1 6
2 3
2 6
3 5
2 5

9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

"""