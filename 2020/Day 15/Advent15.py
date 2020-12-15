import functools

input = [8,11,0,19,1,2]
tests = [[0,3,6], [1,3,2], [2,1,3]]

def get_at_index(numbers, index=2020):
	last = numbers[-1]
	last_occurances = dict()
	for i in range(len(numbers), index):
		#print(last_num, i, numbers)
		#print(numbers[-1], i)
		#print(i)
		without_last = numbers[0:-1]
		if last not in without_last:
			last = 0
		else:
			last_occurance = len(numbers) - (without_last[::-1].index(last)) - 1
			#print(last_occurance, i)
			last = i - last_occurance
		numbers.append(last)
	return numbers[-1]
#for test in tests:
#	print(get_at_index(2020, test))
print(get_at_index(input))
