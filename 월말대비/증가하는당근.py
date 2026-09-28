T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    C += [0]
    ans = 1
    temp = 1
    for i in range(1, N):
        if C[i]>C[i-1]:
            temp += 1
        if C[i]>=C[i+1]:
            if ans < temp:
                ans = temp
            temp = 1
        print(C[i], ans, temp)
    print(f'#{tc} {max(temp, ans)}')


"""
2
12
1 2 3 4 3 4 5 6 2 3 4 5
8
1 3 5 2 4 6 7 8
"""