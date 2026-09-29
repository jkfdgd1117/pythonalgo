T = int(input())
for tc in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split()))
    heap = [0, temp[0]]
    
    for i in range(1, N):
        heap.append(temp[i])
        k = i+1
        while heap[k//2] > heap[k]:
            heap[k//2], heap[k] = heap[k], heap[k//2]
            k = k//2
    ans = 0
    while N != 1:
        N = N//2
        ans += heap[N]
    print(f'#{tc} {ans}')


"""
3
7
7 2 5 3 4 6 1
6
3 1 4 16 23 12
11
18 57 11 52 14 45 63 40 41 55 58


"""
