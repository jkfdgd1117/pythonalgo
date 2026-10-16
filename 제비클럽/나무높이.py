def go(day):
    global ans, anju
    if trees.count(target+1):
        return
    if day >= ans:
        return
    if trees.count(target) == N:
        ans = day-1
        return
    if day % 2:
        grow = 1
    else:
        grow = 2
    for i in range(N+1):
        if i != N:
            if trees[i] == target:
                continue
            if trees[i] > target:
                return
        if i == N:
            if anju:
                continue
        trees[i] += grow
        if i == N:
            anju = True
        go(day+1)
        trees[i] -= grow
        if i == N:
            anju = False
    
        
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    target = max(trees)
    trees.append(1557)
    ans = float('inf')
    anju = False
    if trees.count(target) == N:
        print(f'#{tc} 0')
        continue
    go(1)
    print(f'#{tc} {ans}')
    
    
    


"""
10
2
5 5
2
4 2
2
3 4
4
2 3 10 5
4
1 2 3 4
20
26 19 23 2 24 2 17 15 1 27 6 29 18 23 27 13 26 21 9 1
20
4 5 3 4 2 4 4 3 5 2 2 3 5 5 5 2 5 2 5 5
20
1 3 6 5 5 1 5 4 3 5 4 2 4 6 5 5 4 5 5 3
20
4 5 6 6 5 3 1 3 3 3 3 5 3 3 3 4 5 1 4 3
20
26 6 8 15 10 15 14 6 19 16 5 13 9 12 14 29 28 3 12 27

N<=100, 나무높이(tr)<=120

하루에 한 나무씩 물을 줄 수 있는데
홀수날은 물주면 나무 키가 1 자라고
짝수날은 물주면 나무 키가 2 자람
어떤 날은 물을 안줄수도있음
모든 나무가 맨처음 가장 큰 나무와 키가 같아져야함
가능한 최소 날짜 수를 출력

물을 준다/안준다로 재귀하는데
제일 높은 나무는 아마 물 안줘도 될거같음

visited 대신 tr == target 으로 검사하면 될듯?

근데 중요한게 나무에 물을 안주는경우를 생각해야하는데
그거는 가짜나무를 하나 만들어서 거기에 물주는식으로 하면 해결될거같음

그리고 계속 물을 안주면서 무한루프들어가는 경우를 제어해야함
근데 생각해보면 이틀 연속 물을 안주는경우는 없을거니까 그걸 제어하면 될거같음
전날 물을 안줬는지를 변수로 확인할거임
"""
