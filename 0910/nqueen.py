dr = [0, 1, 1, 1, 0, -1, -1, -1] 
dc = [1, 1, 0, -1, -1, -1, 0, 1]
def start(r, c):
    global queens, valid, ans, board
    if queens == N:
        ans += 1
        print(*board, sep='\n')
        print('='*10)
        queens = 0
        return
    if board[r][c] in (1, 2):
        start(r, c+1)
        return
    else:
        board[r][c] = 2
        queens += 1
        valid = True
        for i in range(8): 
            if valid:
                tenkai(r+dr[i], c+dc[i], i)
        start(r+1, 1)        
    return

def tenkai(r, c, d):
    global valid, board
    if board[r][c] == 3:
        return
    elif board[r][c] == 1:
        tenkai(r+dr[d], c+dc[d], d)
    elif board[r][c] == 2:
        valid = False
        return
    elif board[r][c] == 0:
        board[r][c] = 1
        tenkai(r+dr[d], c+dc[d], d)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = 0
    for i in range(N):
        queens = 0
        board = [[3]*(N+2)]
        board += [[3] + [0]*N + [3] for _ in range(N)]
        board.append([3]*(N+2))
        start(1, 1+i)
    print(f'#{tc} {ans}')


"""
0 : 아무것도없는곳
1 : 어떤 퀸 범위 안에 드는곳
2 : 퀸 있는곳
3 : 패딩
체스판 전부 돌면서 퀸 놓을자리 탐색
0이면 퀸 설치 -> 퀸 범위따라 1로 영역전개 후 다음 
나머지면 패스

영역전개 해나가다가
0이면 1로 변경
1이면 패스
2면 케이스 폐기
3이면 영역전개 중지

0 1 2 3 4 5 6 7 8 9

1 1

2 0

3 0

4 2

5

6

7

8
"""