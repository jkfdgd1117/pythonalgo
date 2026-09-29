def go(w):
    global num
    if w>N:
        return
    
    go(w*2)
    tree[w] = num
    num += 1
    go(w*2+1)
    
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    num = 1
    go(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
    
    
"""

3
6
8
15

"""
