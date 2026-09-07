T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    ans = 0
    for s in str1:
        if ans < str2.count(s):
            ans = str2.count(s)
    print(f'#{tc} {ans}')