T = int(input())
for tc in range(1, T+1):
    text = list(input().split())
    stack = []
    ans = 0 
    for t in text:
        if t.isdecimal():
            stack.append(int(t))
        elif t == '.':
            ans = stack.pop()
            if stack:
                ans = 'error'
            break
        elif (t not in '+-*/') or (len(stack) < 2):
            ans = 'error'
            break
        elif t == '+':
            stack.append(stack.pop()+stack.pop())
        elif t == '-':
            stack.append((stack.pop()-stack.pop())*(-1))
        elif t == '*':
            stack.append(stack.pop()*stack.pop())
        elif t == '/':
            temp = stack.pop()
            stack.append(int(stack.pop()/temp))
        
    print(f'#{tc} {ans}')



"""

3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .


"""