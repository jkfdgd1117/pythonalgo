T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    counts = [0]*(max(num)+1)
    for i in num:
        counts[i] += 1
    newnum = []
    for idx, j in enumerate(counts):
        for _ in range(j):
            newnum.append(idx)
    print(f'#{tc}', *newnum)
"""
    선택정렬
    N = int(input())
    num = list(map(int, input().split()))
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if num[min_idx] > num[j]:
                min_idx = j
        num[min_idx], num[i] = num[i], num[min_idx]
    print(f'{tc}', *num)
"""

"""
    버블정렬
    N = int(input())
    num = list(map(int, input().split()))
    for i in range(N-1):
        for j in range(N-i-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    print(f'{tc}', *num)
"""

"""
    카운팅정렬
    N = int(input())
    num = list(map(int, input().split()))
    counts = [0]*(max(num)+1)
    for i in num:
        counts[i] += 1
    newnum = []
    for idx, j in enumerate(counts):
        for _ in range(j):
            newnum.append(idx)
    print(f'#{tc}', *newnum)
"""