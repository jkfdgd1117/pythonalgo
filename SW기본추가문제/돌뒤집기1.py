T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    stones = list(input().split())
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        for w in range(j):
            if i >= N-1:
                break
            stones[i+1] = stones[i]
            i += 1
    ans = ' '.join(stones)
    print(f'#{tc} {ans}')