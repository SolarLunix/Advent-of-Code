import numpy as np 

my_file = "/home/solarlunix/Documents/AdventOfCode2023/adventofcode2023/inputs/Dec1/dec1.txt"
total = 0

written = {
	"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

with open(my_file) as f:
	for line in f:
		numbers = []
		for i, val in enumerate(line):
			if val.isdigit():
				numbers.append((val))
			else:
				for key, value in written.items():
					if line[i:].startswith(key):
						numbers.append(value)
		#print(numbers)
		#print(numbers[0] + numbers[-1])
		try:
			total += (int)(numbers[0] + numbers[-1])
		except Exception as e:
			print(line)

print("The total is: ", total)