dr = [0, -1, 0, 1, 0]   # 정 상 우 하 좌
dc = [0, 0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    mA = list(map(int, input().split()))
    mB = list(map(int, input().split()))
    grid = [[set() for _ in range(10)] for _ in range(10)]
    test = [[0]*10 for _ in range(10)]
    Ar, Ac = 0, 0
    Br, Bc = 9, 9
    ans = 0
    
    APs = []
    for i in range(A):
        Pc, Pr, K, P= map(int, input().split())
        Pr -= 1
        Pc -= 1
        APs.append(P)
        for r in range(-K, K+1):
            width = K - abs(r)
            for c in range(-width, width+1):
                if (0<=Pr+r<10) and (0<=Pc+c<10):
                    grid[Pr+r][Pc+c].add(i)
    if grid[Ar][Ac]:
        charge = 0
        for c in grid[Ar][Ac]:
            charge = max(APs[c], charge)
        ans += charge
    if grid[Br][Bc]:
        charge = 0
        for c in grid[Br][Bc]:
            charge = max(APs[c], charge)
        ans += charge
    for t in range(M):
        test[Ar][Ac] += 1
        test[Br][Bc] += 1
        
        Ar += dr[mA[t]]
        Ac += dc[mA[t]]
        Br += dr[mB[t]]
        Bc += dc[mB[t]]

        if grid[Ar][Ac] & grid[Br][Bc]:
            temp = 0
            for tempA in grid[Ar][Ac]:
                for tempB in grid[Br][Bc]:
                    if tempA == tempB:
                        temp = max(temp, APs[tempA])
                    else:
                        temp = max(temp, APs[tempA]+APs[tempB])
            ans += temp
        else:
            if grid[Ar][Ac]:
                charge = 0
                for c in grid[Ar][Ac]:
                    if charge < APs[c]:
                        charge = APs[c]
                ans += charge  
            if grid[Br][Bc]:
                charge = 0
                for c in grid[Br][Bc]:
                    if charge < APs[c]:
                        charge = APs[c]
                ans += charge
    print(f'#{tc} {ans}')
        


"""

2
20 3
2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
4 4 1 100
7 10 3 40
6 3 2 70
60 4
0 3 3 3 0 1 2 2 2 1 2 2 3 3 4 4 0 3 0 1 1 2 2 3 2 2 3 2 2 0 3 0 1 1 1 4 1 2 3 3 3 3 3 1 1 4 3 2 0 4 4 4 3 4 0 3 3 0 3 4 
1 1 4 1 1 1 1 1 1 4 4 1 2 2 3 2 4 0 0 0 4 3 3 4 3 3 0 1 0 4 3 0 4 3 2 3 2 1 2 2 3 4 0 2 2 1 0 0 1 3 3 1 4 4 3 0 1 1 1 1 
6 9 1 180
9 3 4 260
1 4 1 500
1 3 1 230

// 총 테스트 케이스 개수 T=5
// 첫 번째 테스트 케이스: M=20, A=3
// 사용자A의 이동 정보
// 사용자B의 이동 정보
// AP 1의 정보 (4, 4), C1=1, P1=100
// AP 2의 정보 (7, 10), C2=3, P2=40
// AP 3의 정보 (6, 3), C3=2, P3=70

set() set() set() set() set() set() {1} {1} {1} {1}
{3} set() set() set() set() {1} {1} {1} {1} {1}
{2, 3} {3} set() set() {1} {1} {1} {1} {1} {1}
{2, 3} {2} set() set() set() {1} {1} {1} {1} {1}
{2} set() set() set() set() set() {1} {1} {1} {1}
set() set() set() set() set() set() set() {1} {1} {1}
set() set() set() set() set() set() set() set() {1} set()
set() set() set() set() set() {0} set() set() set() set()
set() set() set() set() {0} {0} {0} set() set() set()
set() set() set() set() set() {0} set() set() set() set()

한 칸에 세개 이상 충전 범위가 겹칠 수 있는걸 생각해야함

1. 현재 칸에 충전범위 한가지만 있으면 다른 사용자랑 충전기 같은거인지 확인
1-1. 다른거면 그냥 충전함
1-2. 같은거면 1/2 해서 충전함

2. 현재 칸에 충전범위 두개 이상 있으면 다른 사용자랑 충전기 교집합이 공집합인지 확인
2-1. 교집합 없으면 제일 많이주는거 쓰기
2-2. 있으면 경우의 수 따져야함

경우의 수 따지기
A가 할수있는곳 1 2 3 4 5 있고
B가 할수있는곳 3 4 5 6 7 8 있다고 하면
경우의 수 5*6=30개 충전할수있는곳 개수 최대 8이니 아무리많아도 이론상 64개 가는길 내내 한다고해도 최대 6400번



"""