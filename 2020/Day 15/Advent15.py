import functools

input = [8,11,0,19,1,2]
tests = [[0,3,6], [1,3,2], [2,1,3]]

def get_at_index(numbers, index=2020):
	last = numbers[-1]
	numbers = numbers[0:-1]
	last_occurances = dict()
	for i in range(len(numbers)):
		last_occurances[numbers[i]] = (i,i)
	#print(last_occurances)
	for i in range(len(numbers), index):
		#print(last_occurances, i)
		if last not in last_occurances.keys():
			numbers.append(last)
			last_occurances[last] = (i,i)
			last = 0
		else:
			numbers.append(last)
			last_occurances[last] = (last_occurances[last][1], i)
			last = i - last_occurances[last][0]
	return numbers[-1]

#print(get_at_index(tests[0]))
print(get_at_index(input,30000000))
