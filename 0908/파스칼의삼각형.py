tri = []
tri.append([1])
tri.append([1,1])
for level in range(3, 11):
    temp = [1]
    for i in range(1, level-1):
        temp.append(tri[level-2][i-1]+tri[level-2][i])
    temp += [1]
    tri.append(temp)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    for j in range(N):
        print(*tri[j])