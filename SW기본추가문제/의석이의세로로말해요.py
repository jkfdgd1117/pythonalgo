T = int(input())
for tc in range(1, T+1):
    text = []
    for _ in range(5):
        temp = list(input())
        while len(temp) < 15:
            temp.append('똥')
        text.append(temp)
    ans = ''
    for c in range(15):
        for r in range(5):
            if text[r][c] != '똥':
                ans += text[r][c]
    print(f'#{tc} {ans}')
