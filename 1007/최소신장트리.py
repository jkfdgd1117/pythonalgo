import heapq

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    n += 1
    arr = [[] for _ in range(n)]

    for _ in range(m):
        start, end, cost = map(int, input().split())
        arr[start].append((cost, end))
        arr[end].append((cost, start))
        
    used = [0]*n
    heap = []

    heapq.heappush(heap, (0, 0)) # 비용, 정점

    total = 0   # 비용합
    cnt = 0     # MST에 포함된 정점수

    while heap:
        cost, now = heapq.heappop(heap)
        
        if used[now]:
            continue
        used[now] = 1
        total += cost
        cnt += 1
        
        for next_cost, next_node in arr[now]:
            if not used[next_node]:
                heapq.heappush(heap, (next_cost, next_node))
    print(f'#{tc} {total}')
    
    
"""
3
2 3
0 1 1
0 2 1
1 2 6
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
