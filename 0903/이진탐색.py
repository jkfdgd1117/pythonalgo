def binary(N, key):
    step = 0
    l = 1
    r = N
    while l <= r:
        c = (l + r) // 2
        step += 1
        if c == key:
            return step
        elif c > key:
            r = c
        else:
            l = c


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    result = '0'
    StepA = binary(P, A)
    StepB = binary(P, B)
    if StepA > StepB:
        result = 'B'
    elif StepA < StepB:
        result = 'A'
    print(f'#{tc} {result}')
