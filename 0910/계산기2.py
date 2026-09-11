for tc in range(1, 11):
    N = int(input())
    text = list(input())
    nums = []
    opr = []
    hap = 0
    gop = 0
    text.append('end')
    for i, t in enumerate(text):
        if t == 'end':
            break
        if t.isdecimal():
            nums.append(int(t))
        else: 
            opr.append(t)
            if t == '+':
                hap += 1
            if t == '*':
                gop += 1
        if (len(nums) == 1+hap+gop) and (text[i+1] != '*'):
            while opr:
                op = opr.pop()
                if op == '+':
                    nums.append(nums.pop()+nums.pop())
                    hap -= 1
                elif op == '*':
                    nums.append(nums.pop()*nums.pop())
                    gop -= 1
    print(f'#{tc} {nums[0]}')