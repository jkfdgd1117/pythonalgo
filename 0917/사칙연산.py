def go(now):
    if not tree[now][1]:
        stack.append(tree[now][0])
        return
    go(tree[now][1])
    go(tree[now][2])
    if tree[now][0] == '+':
        t1 = stack.pop()
        t2 = stack.pop()
        stack.append(t1+t2)
    elif tree[now][0] == '-':
        t1 = stack.pop()
        t2 = stack.pop()
        stack.append(t2-t1)
    elif tree[now][0] == '*':
        t1 = stack.pop()
        t2 = stack.pop()
        stack.append(t1*t2)
    elif tree[now][0] == '/':
        t1 = stack.pop()
        t2 = stack.pop()
        stack.append(t2/t1)  


for tc in range(1, 11):
    N = int(input())
    tree = [[0]*3 for _ in range(N+1)]
    for _ in range(N):
        temp = input().split()
        temp[0] = int(temp[0])
        if temp[1].isdecimal():
            tree[temp[0]][0] = int(temp[1])
        else:
            tree[temp[0]][0] = temp[1]
            tree[temp[0]][1] = int(temp[2])
            tree[temp[0]][2] = int(temp[3])
    stack = []
    go(1)
    print(f'#{tc} {int(stack.pop())}')
    

"""
트리 후위순회한다음  계산기에 넣으면 될거같음

5
1 - 2 3
2 - 4 5
3 10
4 88
5 65
7
1 / 2 3
2 - 4 5
3 - 6 7
4 261
5 61
6 81
7 71

인접행렬?
3*N 행렬에 데이터, left, right 넣으면 될거같음


"""
