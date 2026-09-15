def rsp(A, B): # 가위 1 묵 2 보 3
    if B == (A%3)+1: # 1을 이기는건 2 3을 이기는건 1
        return B
    else:
        return A

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    haksang = list(map(int, input().split()))
    # 이진탐색 스택 잘 쓰면 풀릴듯