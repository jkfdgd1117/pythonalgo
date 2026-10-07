# 1. branch N 인덱스 조합 만들어서 각 경우의 시너지 계산
# 2. 숫자가 하나도 안 겹치는 조합끼리 차이 구하기

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sy = float('inf')

    for tar in range(1<<N):
        sub = []
        for i in range(N):
            if tar & 1:
                sub.append(i)
            tar >>= 1

        if len(sub) == (N//2):
            # 집합 두 개로 나누어서
            sub2 = [x for x in range(N) if x not in sub]
            sy1 = 0
            sy2 = 0

            for r in range(N//2):
                for c in range(N//2):
                    if r!= c:
                        sy1 += arr[sub[r]][sub[c]]
                        sy2 += arr[sub2[r]][sub2[c]]

            diff = abs(sy1-sy2)
            min_sy = min(diff, min_sy)

    print(f"#{tc} {min_sy}")