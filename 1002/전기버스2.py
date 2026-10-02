def drive(i, cnt):
    global min_cnt
    if (cnt-1) >= min_cnt:
        return
    if i >= N:

        min_cnt = min(cnt - 1, min_cnt)
        return

    for j in range(bus_stop[i], 0, -1):
        drive(i + j, cnt + 1)
        
T = int(input()) 
for tc in range(1, T + 1):
    N, *bus_stop = map(int, input().split())

    bus_stop = [0] + bus_stop

    min_cnt = float('inf')

    drive(1, 0)
 
    print(f"#{tc} {min_cnt}")