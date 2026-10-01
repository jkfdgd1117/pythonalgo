def bins(key):
    global ans
    left = 0
    right = N-1
    mid = (left+right)//2
    if table[mid] == key:
        ans += 1
        return
    d = None
    while left<=right:
        mid = (left+right)//2
        if table[mid] == key:
            ans += 1
            break
        elif table[mid] < key:
            left = mid + 1
            if d == True:
                break
            d = True
            continue
        elif table[mid] > key:
            right = mid - 1
            if d == False:
                break
            d = False
            continue
    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = list(map(int, input().split()))
    table = sorted(table)
    keys = list(map(int, input().split()))
    ans = 0
    for k in keys:
        bins(k)
    print(f'#{tc} {ans}')




"""

3
3 3
1 2 3
2 3 4
4 5
1 3 5 7
2 4 6 8 10
5 5
2 3 5 7 9
1 2 3 4 5
"""
