def go(r, c, score):
    global ans
    if ans <= score:
        return
    if (r==(N-1)) and (c==(N-1)):
        if ans > score:
            ans = score
        return
    
    if c < N-1:
        go(r, c+1, score+grid[r][c+1])
    if r < N-1:
        go(r+1, c, score+grid[r+1][c])
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    
    ans = float('inf')
    go(0, 0, grid[0][0])
    print(f'#{tc} {ans}')


"""
그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.

맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.

그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.

3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1
"""
