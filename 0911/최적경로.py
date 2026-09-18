def dist(A, B): # 점 A와 B의 거리 반환
    return abs(A[0]-B[0])+abs(A[1]-B[1])

def visit(total): # customers로 만들 수 있는 길이 N의 순열의 가짓수
    global ans
    if total >= ans:
        return
    if len(route) == N+1:
        total += dist(route[-1], home)
        if ans > total:
            ans = total
        return
    for j in range(0, N):
        if customers[j] not in route:
            route.append(customers[j])
        else:
            continue
        visit(total+dist(route[-2], route[-1]))
        route.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    work = [arr[0], arr[1]]
    home = [arr[2], arr[3]]
    customers = [] # 길이 : N
    for i in range(4, N*2+3, 2): # 4 6 8 10 ... N*2 N*2+2
        customers.append([arr[i], arr[i+1]])
    route = [work] # 길이 : N+1 (마지막에 home이랑 거리잴거임)
    ans = 99999
    visit(0)
    print(f'#{tc} {ans}')


"""
3
5
0 0 100 100 70 40 30 10 10 5 90 70 50 20
6
88 81 85 80 19 22 31 15 27 29 30 10 20 26 5 14
10
39 9 97 61 35 93 62 64 96 39 36 36 9 59 59 96 61 7 64 43 43 58 1 36

1 2 3로 순열 만든다고 하면
6가지
123
132
213
231
312
321

"""