T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    ans = -1
    if (C > 2) and (B > 1):
        if B >= (C-1):
            ans += (B - (C - 1))
            B = C-1
        if A >= B:
            if A >= (C-2):
                ans += (A - (C - 2))
                A = C-2
        ans += 1
    print(f'{tc} {ans}')
    






"""
C가 2이하면 -1
B가 1이하면 -1

C-2, C-1, C 형태로 만들어야함

4 5 6 >
4 6 5 > 4 4 5 > 3 4 5
5 4 6 > 3 4 6
5 6 4 > 5 3 4 > 2 3 4
6 4 5 > 3 4 5
6 5 4 > 6 3 4 > 2 3 4

2 3 4 > 
2 4 3 > 2 2 3 > 1 2 3
3 2 4 > 1 2 4
3 4 2 > x
4 2 3 > 1 2 3
4 3 2 > x


"""