T = int(input())
for tc in range(1, T+1):
    code = input()
    pair = { "{" : "}" , "(" : ")" }
    stack = []
    ans = 1
    for c in code:
        if c in "{(":
            stack.append(c)

        if c in "})":
            if not stack:
                ans = 0
                break
            left = stack.pop()
            if pair[left] != c:
                ans = 0
                break
    if stack:
        ans = 0
    print(f'#{tc} {ans}')