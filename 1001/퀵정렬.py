def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    a = 1
    b = len(arr)-1
    while a <= b:
        if arr[a] < pivot:
            a += 1
            continue
        if arr[b] > pivot:
            b -= 1
            continue
        arr[a], arr[b] = arr[b], arr[a]
        a += 1
        b -= 1
    arr[b], arr[0] = arr[0], arr[b]
    return quick_sort(arr[:b]) + [arr[b]] + quick_sort(arr[b+1:])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    target = list(map(int, input().split()))
    target = quick_sort(target)
    print(f'#{tc} {target[N//2]}')


"""

2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8

    퀵정렬이란
    피벗
    a, b 있는데

    피벗 0 
    a = 피벗+1
    b = -1
    a는 왼쪽에서 오면서 피벗보다 큰값, b는 오른쪽에서 오면서 피벗보다 작은값 찾을거임
    찾으면 서로 위치바꿈
    더 못찾아서 둘이 만나면 a+1이랑 피벗이랑 바꿈

    이거 한번하면 왼쪽엔 피벗보다 작은거 오른쪽엔 피벗보다 큰거 남게됨

    그다음 왼쪽이랑 오른쪽에 똑같은거 하면됨
""" 
