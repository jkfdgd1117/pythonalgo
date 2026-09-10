dr = [0, 1, 1, 1, 0, -1, -1, -1] 
dc = [1, 1, 0, -1, -1, -1, 0, 1]
def start(r, c):
    global queens, valid
    if board[r][c] == 1 or board[r][c] == 2:
        return
    else:
        board[r][c] = 2
        queens += 1
        for i in range(8):
            if valid:
                tenkai(r, c, i)
            return
    return
def tenkai(r, c, d):
    global valid
    if board[r][c] == 2:
        valid = False
        return
    elif board[r][c] == 1:
        tenkai(r+dr[d], c+dc[d], d)
    elif board[r][c] == 3:
        return
    elif board[r][c] == 0:
        board[r][c] = 1
        tenkai(r+dr[d], c+dc[d], d)

    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[3]*(N+2)]
    board += [[3] + [0]*N + [3] for _ in range(N)]
    board.append([3]*(N+2))
    queens = 0
    valid = True
    start(1, 1)


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


"""