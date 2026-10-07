def lead(student):
    if team[student] != student:
        team[student] = lead(team[student])
    return team[student]
    
def union(x, y):
    kx = lead(x)
    ky = lead(y)
    team[ky] = kx

    
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    aps = list(map(int, input().split()))
    team = list(range(N+1))
    ans = 0
    for i in range(M):
        union(aps[i*2], aps[i*2+1])
    for j in range(1, N+1):
        if team[j] == j:
            ans += 1
    print(f'#{tc} {ans}')

"""
4
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
4 4
1 2 2 3 3 4 4 1

12 34 이렇게 신청서가 온것


"""
