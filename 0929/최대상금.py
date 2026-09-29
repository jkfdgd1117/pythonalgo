T = int(input())
for tc in range(1, T + 1):
	number, change = input().split()
	current = {number}

	for count in range(int(change)):
		next_case = set()
		for state in current:
			for i in range(len(state)-1):
				for j in range(i+1, len(state)):
					temp = list(state)
					temp[i], temp[j] = temp[j], temp[i]
					new_state = ''.join(temp)
					next_case.add(new_state)
		current = next_case
	print(f'#{tc} {max(current)}')