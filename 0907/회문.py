T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(input())
    ans = ''
    for i in range(N):
        for w in range(N-M+1):
            
            for k in range(M//2):
                if arr[i][w+k] != arr[i][w+M-k-1]:
                    break
            else:
                ans = arr[i][w:w+M]
    for w in range(N):
        for i in range(N-M+1):
            for k in range(M//2):
                if arr[i+k][w] != arr[i+M-k-1][w]:
                    break
            else:
                for l in range(M):
                    ans += arr[i+l][w]
    print(f'#{tc} {ans}')