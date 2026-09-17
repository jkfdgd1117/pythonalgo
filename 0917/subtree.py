def preorder(t):
        global count
        if t:
            count += 1
            preorder(left[t])
            preorder(right[t])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E+1
    left = [0] * (V+1)
    right = [0] * (V+1)
    tree = list(map(int, input().split()))
    for i in range(E):
        p = tree[i*2]
        c = tree[i*2+1]
        if left[p] == 0: # 왼쪽 자식 없으면
            left[p] = c
        else:
            right[p] = c

    count = 0
    preorder(N)
    print(f'#{tc} {count}')


"""

3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10

"""