def banji(start):
    if start >= (len(text)-1):
        return
    if text[start] == text[start+1]:
        del text[start]
        del text[start]
        banji(start-1)
    else:
        banji(start+1)
T = int(input())
for tc in range(1, T+1):
    text = list(input())
    text = ['AA'] + text
    banji(1)
    print(f'#{tc} {len(text)-1}')