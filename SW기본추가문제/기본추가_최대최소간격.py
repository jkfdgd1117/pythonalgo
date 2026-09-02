T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    minidx = arr.index(min(arr))
    arr.reverse()
    maxidx = arr.index(max(arr))
    maxidx = N - maxidx - 1
    print(abs(maxidx-minidx))