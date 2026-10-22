dr = [0, 1, 0, -1]  # 우 하 좌 상 (R D L U)
dc = [1, 0, -1, 0]
dirs = {'R':0, 'D':1, 'L':2, 'U':3}
head = ['>', 'v', '<', '^']
blocked = ['*', '#', '-']

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(list(input()))
    for r in range(H):
        for c in range(W):
            if grid[r][c] in head:
                nr = r
                nc = c
                
    N = int(input())
    act = input()
    for a in act:
        if a in dirs:
            d = dirs[a]
            grid[nr][nc] = head[d]
            if (0<=nr+dr[d]<H) and (0<=nc+dc[d]<W):
                if grid[nr+dr[d]][nc+dc[d]] not in blocked:
                    grid[nr][nc] = '.'
                    nr += dr[d]
                    nc += dc[d]
                    grid[nr][nc] = head[d]
        else:
            d = head.index(grid[nr][nc])
            br = nr
            bc = nc
            while (0<=br+dr[d]<H) and (0<=bc+dc[d]<W):
                br += dr[d]
                bc += dc[d]
                if grid[br][bc] == '#':
                    break 
                if grid[br][bc] == '*':
                    grid[br][bc] = '.'
                    break
    print(f'#{tc}', ''.join(grid[0]))
    for i in range(1, H):
        print(''.join(grid[i]))
        
                
            
    

    
    
"""
1
3 7
***....
*-..#**
#<.****
23
SURSSSSUSLSRSSSURRDSRDS


문자	의미
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)

0. 상하좌우 이동하는거 만들기
- 이동할때 방향전환 해야함
- 이동할때 갈 수 있는 곳인지 확인해야함
- 이동할때 맵 밖인지 확인해야함
1. 벽돌 부시는거 만들기
2. 강철에 포탄 막히는거 만들기



"""
