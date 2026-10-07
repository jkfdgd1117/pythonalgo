from heapq import heappop, heappush

def dijkstra(s): # s : 시작 정점 번호, s에서 시작해서 다른 모든 정점까지의 최단거리 구하는게 목표
    heap = []
    heappush(heap, (0, s))
    D[s] = 0
    while heap:
        w, v = heappop(heap)
        if w > D[v]:
            continue
        for nv, nw in G[v]:
            newdist = w + nw
            if D[nv] > newdist:
                D[nv] = newdist
                heappush(heap, (newdist, nv))
    pass
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    V += 1
    G = [[] for _ in range(V)] # 인접 리스트 사용 (인접 행렬 쓸거면 무한대로 초기화)

    for i in range(E):
        s, e, w = map(int, input().split())
        G[s].append((e, w))
        
    D = [float('inf')]*V

    dijkstra(0)

    print(f'#{tc} {D.pop()}')
    
"""
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
"""
