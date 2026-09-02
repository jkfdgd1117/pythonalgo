T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    new = ' '.join(map(str, arr))
    print(f'#{tc} {new}')