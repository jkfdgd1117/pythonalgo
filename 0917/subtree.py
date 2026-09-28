def go(n):
    count = 1
    stack = []
    if tree[0][n]:
        count += 1
        stack.append(tree[0][n])
    if tree[1][n]:
        count += 1
        stack.append(tree[1][n])
    while stack:
        j = stack.pop()
        if tree[0][j]:
            count += 1
            stack.append(tree[0][j])
        if tree[1][j]:
            count += 1
            stack.append(tree[1][j]) 

    return count   

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0]*(max(temp)+1) for _ in range(2)]
    for i in range(E):
        bumo = temp[i*2]
        jasik = temp[i*2+1]
        if not tree[0][bumo]:
            tree[0][bumo] = jasik
        else:
            tree[1][bumo] = jasik
    ans = go(N)
    print(f'#{tc} {ans}')


"""

3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10

"""