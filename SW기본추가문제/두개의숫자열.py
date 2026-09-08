T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    if N <= M:
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
    else:
        B = list(map(int, input().split()))
        A = list(map(int, input().split())) # 둘중 더 짧은게 무조건 A로 들어감
    gin = max(N, M)
    zarp = min(N, M)
    ans = 0
    for w in range((gin - zarp)+1):
        haps = 0
        for i in range(zarp):
            haps += A[i]*B[i+w]
        if ans < haps:
            ans = haps
    print(f'#{tc} {ans}')
