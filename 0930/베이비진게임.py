def check(cards):
    for w in cards:
        if w >= 3:
            return True
    for j in range(8):
        if cards[j] and cards[j+1] and cards[j+2]:
            return True
        

T = int(input())
for tc in range(1, T+1):
    M = list(map(int, input().split()))
    p1 = [0]*10
    p2 = [0]*10
    ans = 0
    for i in range(len(M)):
        if not i%2:
            p1[M[i]] += 1
            if check(p1):
                ans = 1
                break
        else:
            p2[M[i]] += 1
            if check(p2):
                ans = 2
                break
    print(f'#{tc} {ans}')



"""
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3

5 2 1 2 9 0
3 9 5 0 2 0
"""