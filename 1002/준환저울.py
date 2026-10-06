def go(weights, now, remain):
    global ans
    if weights >= remain:
        k = N - now
        ans += factorial[k] * power2[k]
        return
    for i in range(now, N):
        w = chus[i]
        chus[now], chus[i] = chus[i], chus[now]
        go(weights+w, now+1, remain-w)
        if weights >= w:
            go(weights-w, now+1, remain-w)
        chus[now], chus[i] = chus[i], chus[now]

factorial = [1]
power2 = [1]
for i in range(1, 10):
    factorial.append(factorial[-1]*i)
    power2.append(power2[-1]*2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    chus = list(map(int, input().split()))
    ans = 0
    go(0, 0, sum(chus))
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

lsum - rsum 을 weights로 치환해서 하나로 넘김

remain도 넘김
"""