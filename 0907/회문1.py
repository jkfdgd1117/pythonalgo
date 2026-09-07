for tc in range(1,11):
    N = int(input())
    arr = []
    for _ in range(8):
        arr.append(input())
    ans = 0
    for i in range(8):
        for w in range(9-N):
            for k in range(N//2):
                if arr[i][w+k] != arr[i][w+N-k-1]:
                    break
            else:
                ans += 1
    for w in range(8):
        for i in range(9-N):
            temp = ''
            for k in range(N//2):
                if arr[i+k][w] != arr[i+N-k-1][w]:
                    break
            else:
                for l in range(N):
                    temp += arr[i+l][w]
            if temp:
                ans += 1
    print(f'#{tc} {ans}')