# A음식 리스트 에 들어가지 않은 값은 B음식 리스트에 넣는다.
# visited를 이용해서 들어갔는지 안들어갔는지 구한다.

def get_sum(food):  # 이 함수에 들어가는 것은 A_food 리스트, B_food 리스트
    total = 0
    for i in range(len(food) - 1):
        for j in range(i+1, len(food)):
            a = food[i]
            b = food[j]
            total += arr[a][b] + arr[b][a]
    return total

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N       # A리스트에 들어있는지 없는지 확인하기 위한 visited 변수
    min_sum = float("inf")
    def abc(level, start):
        global min_sum
        # 종료 조건
        if level == N//2:
            A_food = []
            B_food = []
            for i in range(N):
                if visited[i]:
                    A_food.append(i)
                else:
                    B_food.append(i)
            A_food_sum = get_sum(A_food)
            B_food_sum = get_sum(B_food)
            min_sum = min(min_sum, abs(A_food_sum - B_food_sum))
            return
        # 재귀 호출
        for i in range(start, N):
            visited[i] = 1
            abc(level+1, i+1)
            visited[i] = 0
    abc(0, 0)
    print(f'#{t} {min_sum}')