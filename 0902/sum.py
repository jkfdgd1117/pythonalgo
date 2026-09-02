for _ in range(1, 11):
    T = int(input())
    arr = []
    for i in range(100):
        row = list(map(int, input().split()))
        arr.append(row)
    arrforcolsum = list(map(list, zip(*arr)))
    max1 = 0
    dia1 = 0
    dia2 = 0
    for i in range(100):
        if sum(arr[i]) >= max1:
            max1 = sum(arr[i])
        if sum(arrforcolsum[i]) >= max1:
            max1 = sum(arrforcolsum[i])
        dia1 += arr[i][i]
        dia2 += arr[i][99-i]
    answer = max(max1, dia1, dia2)
    print(f'#{T} {answer}')