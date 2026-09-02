N = int(input())
boxes = list(map(int, input().split()))
counts = 0
for i, top in enumerate(boxes):
    singlecount = 0
    for check in boxes[i:]:
        if top > check:
            singlecount += 1
    if singlecount >= counts:
        counts = singlecount
print(counts)