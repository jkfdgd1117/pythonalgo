def merge_sort(m):
    if len(m) == 1:
        return m
    
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    global ans
    if left[-1]>right[-1]:
        ans += 1
    li = ri = 0
    result = []
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            result.append(left[li])
            li += 1
        else:
            result.append(right[ri])
            ri += 1
            
    while li < len(left):
        result.append(left[li])
        li += 1
    while ri < len(right):
        result.append(right[ri])
        ri += 1
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    arr = merge_sort(arr)
    print(f'#{tc} {arr[N//2]} {ans}')
    
"""
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
"""
