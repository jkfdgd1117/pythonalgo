def go(lsum, rsum, now, remain):
    global ans
    k = N - now
    if lsum < rsum:
        return
    if lsum - rsum >= remain:
        ans += factorial[k] * (2 ** k)
        return
    if now == N:
        ans += 1
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            go(lsum+chus[i], rsum, now+1, remain-chus[i])
            go(lsum, rsum+chus[i], now+1, remain-chus[i])
            visited[i] = False

factorial = [1]
for i in range(1, 10):
    factorial.append(factorial[-1] * i)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    chus = list(map(int, input().split()))
    ans = 0
    visited = [False]*N
    go(0, 0, 0, sum(chus))
    print(f'#{tc} {ans}')




"""
3
3
1 2 4
3
1 2 3
9
1 2 3 5 6 4 7 8 9

왼쪽에 올리는 경우를 홀수번째
오른쪽에 올리는 경우를 짝수번째 
N = 3일때
1 0 2 0 4 0
2 0 4 0 1 0
4 0 2 0 0 2

무게추들과 같은 갯수의 0을 길이 2N의 순열로 놓는거임
놓으면서 홀수번째 합(Lsum)/짝수번째(Rsum) 합 누적하다가
Lsum < Rsum 되면 return

일단 인자로 몇개 놨는지는 넘겨야함
lsum rsum도 인자로 넘기기?

0들은 순서가 상관없는데 일일히 세는 문제가있음
"""