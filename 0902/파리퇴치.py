T = int(input())
for test_case in range(1, T + 1):
	N, M = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(N)]
	maxcatch = 0
	total = 0
	for scopeY in range(N-M+1):
		for scopeX in range(N-M+1):
			total = 0
			for Y in range(M):
				for X in range(M):
					total += arr[Y+scopeY][X+scopeX]
			if maxcatch <= total:
				maxcatch = total
			if maxcatch == (M**2)*30:
				break
	print(f'#{test_case} {maxcatch}')