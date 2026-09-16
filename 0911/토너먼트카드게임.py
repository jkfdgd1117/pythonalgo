def rsp(A, B):
    if B[1] == (A[1] % 3) + 1:
        return B
    return A


def div(haks):
    if len(haks) == 1:
        return haks[0]
    mid = (len(haks) + 1) // 2
    left = div(haks[:mid])
    right = div(haks[mid:])
    return rsp(left, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    haksang = []
    for idx, card in enumerate(cards):
        haksang.append([idx, card])
    ans = div(haksang)
    print(f'#{tc} {ans[0] + 1}')



"""
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3

밑으로 내려가다보면 2개로 떨어지거나 3개로 떨어지거나 둘중하난데 DP로 풀수있을거같음

한쪽이 3으로 나뉠때 함수를 만들어놓으면 편할거같음(그럴필요없을수도)

N4 = 2, 2
N5 = 3, 2
N6 = 3, 3
N7 = 3, N4
N8 = N4, N4
N9 = N4, N5
...
N13 = N6, N7
...
N25 = N12, N13
...
N50 = N25, N25
...
N100 = N50, N50

아마 최대 8번 나눌듯? 대충 N 범위에 따라 log2(N)+2 정도로 temp 길이 조정하면될것으로보임

근데 뭐가 우승하는진 아는데 얘가 원래 몇번이었는지 알수가없음 지금

맨처음에 각각 학생마다 인덱스를 붙여서 같이넘겨줘야할듯

9 9 9 9 9 9 9 9 9



"""