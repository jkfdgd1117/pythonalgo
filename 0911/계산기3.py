def pfx(text):
    stack = [] # ( + * 들어감
    pfx = []    # 후위계산식 될 예정
    for t in text:
        if t.isdecimal():
            pfx.append(t)       # 숫자는 걍 들어감
        elif t == '(':      
            stack.append(t)     # 여는괄호면 스택에 넣음
        elif t == ')':
            while stack[-1] != '(':     # 닫는괄호면 스택 peek이 (가 나올때까지 스택에 있는거 다 꺼내서 pfx에 넣음
                pfx.append(stack.pop())
            stack.pop() # 다 쓴 여는괄호 버리기
        elif t == '+':  # +면 스택 끝날때까지(여는괄호 나오면 괄호안이었다는거니까 멈춤) 꺼냄
            while stack and stack[-1] != '(':   
                pfx.append(stack.pop()) # 꺼내서 pfx에 넣음 
            stack.append(t) # 지금 더하기 계산 하고 있다는 사실을 스택 맨위에 넣어서 유지함
        elif t == '*':
            while stack and stack[-1] == '*': # 곱하기일때는 다른 곱하기 나올때까지 다곱하면됨
                pfx.append(stack.pop())
            stack.append(t)
        print(stack)
        print(pfx)
    while stack:
        pfx.append(stack.pop()) # 맨 밖에 있는 연산자들은 아직 못들어갔을테니 넣어줌
    return cal(pfx)

def cal(sik):
    stack = []
    for i in sik:
        if i.isdecimal():
            stack.append(int(i))
        else:
            l = stack.pop()
            r = stack.pop()
            if i == '+':
                stack.append(l+r)
            elif i == '*':
                stack.append(l*r)
    return stack.pop()

for tc in range(1, 11):
    N = int(input())
    text = list(input())
    ans = pfx(text)
    print(f'#{tc} {ans}')



"""
(4+8+4*(8*5*(7*(6*8)+3+(6+(3+7+1*7*5*4)*3)*2*3+5)+6+7*7)*4+2+9*4+7+2*3*(7*6*1*8)+9+9)

48+485*768**3+637+17*5*4*+3*+2*3*+5+*6+77*+*4*+2+94*+7+23*76*1*8**+9+9+

"""