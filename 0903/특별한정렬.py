T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    newarr = []
    for i in range(len(arr)):
        if i % 2 == 0:
            newarr.append(arr.pop(arr.index(max(arr))))
        else:
            newarr.append(arr.pop(arr.index(min(arr))))
    ans = newarr[0:10]
    print(f'#{tc}', *ans)


"""
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26
"""