def go(now):
    global ans
    if not tree[now][1]: # 왼쪽자식 없으면(끝단이라는뜻)
        ans += tree[now][0]
        return
    go(tree[now][1])
    ans += tree[now][0]
    if tree[now][2]:
        go(tree[now][2])
    

for tc in range(1, 11):
    N = int(input())
    tree = [[0]*3 for _ in range(N+1)]
    for _ in range(N):                      # tree[n][0] : 데이터, tree[n][1] : left, tree[n][2] : right
        temp = input().split()
        temp[0] = int(temp[0])
        
        tree[int(temp[0])][0] = temp[1]
        if len(temp) == 3:
            tree[int(temp[0])][1] = int(temp[2])
        elif len(temp) == 4:
            tree[int(temp[0])][1] = int(temp[2])
            tree[int(temp[0])][2] = int(temp[3])
    ans = ''
    go(1)
    print(f'#{tc} {ans}')



"""
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
"""
