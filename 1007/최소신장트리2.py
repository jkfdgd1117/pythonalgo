def findboss(m):
    global arr
    if arr[m] == m:
        return m
    root = findboss(arr[m])
    arr[m] = root
    return root

def union(a, b, i):
    global total, cnt
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return
    total += lst[i][2]
    cnt += 1
    arr[fb] = fa
    
    
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    n += 1
    arr = [i for i in range(n)]
    lst = [list(map(int, input().split())) for _ in range(m)]
    lst.sort(key=lambda x:x[2])
    total = 0
    cnt = 0
    for i in range(m):
        if cnt == n-1:
            break
        union(lst[i][0], lst[i][1], i)

    print(f'#{tc} {total}')
    
    
"""
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
"""
