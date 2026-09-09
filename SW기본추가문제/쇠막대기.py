T= int(input())
for tc in range(1, T+1):
    munja = input()
    stick = 0
    jogak = 0
    for i in range(len(munja)):
        if munja[i] == '(':
            if munja[i+1] == '(':
                stick += 1
        if munja[i] == ')':
            if munja[i-1] == '(':
                jogak += stick
            else:
                stick -= 1
                jogak += 1
    print(f'#{tc} {jogak}')