def go(start):
    
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = []
    for _ in range(E):
        graph.append(list(map(int, input().split())))
    S, G = map(int, input().split())
    visited = [0]*(V)
    go(S-1)
    if visited[G-1]:
        ans = 1
    else:
        ans = 0


"""

3
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