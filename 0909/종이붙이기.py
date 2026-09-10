seq = [0]*31
seq[1] = 1
seq[2] = 3
for i in range(3, 31):
    seq[i] = seq[i-1] + (seq[i-2]*2)

T = int(input())
for tc in range(1, T+1):
    ans = int(input())
    print(f'#{tc} {seq[ans//10]}')

"""
10
10
1

20
1010 1010 20
3

30
101010 1020(2) 2010(2) 
3*1 + 1*3 - 1 = 5
5

40
10101010 3010(4) 2020
5*1 + 3*3 - 3 = 11

50

11*1 + 5*3 -5 = 21

"""