T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    ans = len(A) - (A.count(B)*(len(B)-1))
    print(f'#{tc} {ans}')
    