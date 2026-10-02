def make(i, taste, cal):
    global hubo
    if cal > L:
        return
    if i == N:
        if hubo < taste:
            hubo = taste
        return
    if taste + mins[i] < hubo:
        return

    make(i+1, taste+foods[i][0], cal+foods[i][1])
    make(i+1, taste, cal)

T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    foods = []
    for _ in range(N):
        foods.append(list(map(int, input().split())))
    hubo = 0
    mins = []
    for i in range(N):
        hap = 0
        for j in range(i, N):
            hap += foods[j][0]
        mins.append(hap)
    make(0, 0, 0)   # i번째 재료, 누적맛, 누적칼로리
    print(f'#{tc} {hubo}')
    
    
"""
1
5 1000
100 200
300 500
250 300
500 1000
400 400
맛  칼
각 테스트 케이스의 첫 번째 줄에는 재료의 수, 제한 칼로리를 나타내는 N, L가 공백으로 구분되어 주어진다.
 
다음 N개의 줄에는 재료에 대한 민기의 맛에 대한 점수와 칼로리를 나타내는 Ti, Ki가 공백으로 구분되어 주어진다.
"""
