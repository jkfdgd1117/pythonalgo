T = int(input())
for tc in range(1, T+1):
    num = int(input())
    c = [0] * 12   
    for _ in range(6): 
        c[num%10] += 1  
        num //= 10 
    tri = 0
    runc = 0
    result = None
    for i in range(10):
        if c[i] == 6:
            tri += 2
            c[i] -= 6
        elif c[i] == 3:
            tri += 1
            c[i] -= 3
    for i in range(8):
        if c[i] >= 1:
            if (c[i+1] >= 1) and (c[i+2] >= 1):
                runc += 1 
                c[i] -= 1
                c[i+1] -= 1
                c[i+2] -= 1
        if c[i] >= 1:
            if (c[i+1] >= 1) and (c[i+2] >= 1):
                runc += 1 
                c[i] -= 1
                c[i+1] -= 1
                c[i+2] -= 1
    if tri+runc >= 2:
        result = 'Baby Gin'
    else:
        result = 'Lose'
    print(f'#{tc} {result}')


















# T = int(input())
# for tc in range(1, T+1):
#     num = list(map(int, input()))
#     c = [0]*12
#     tri = 0
#     runc = 0
#     result = None
#     for i in range(10):
#         if num.count(i) >= 3:
#             tri += 1
#             for _ in range(3):
#                 num.remove(i)
#     for i in range(8):
#         if num.count(i) >= 1:
#             if (num.count(i+1) >= 1) and (num.count(i+2) >= 1):
#                 runc += 1
#                 num.remove(i)
#                 num.remove(i+1)
#                 num.remove(i+2)
#     if tri+runc >= 2:
#         result = 'Baby Gin'
#     else:
#         result = 'Lose'
#     print(f'#{tc} {result}')