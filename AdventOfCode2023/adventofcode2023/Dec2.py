import numpy as np


my_file = "/home/solarlunix/Documents/Advent-of-Code/AdventOfCode2023/adventofcode2023/inputs/Dec2/dec2.txt"

max_blue = 14
max_red = 12
max_green = 13
valid_games = 0
ids = []
powers = []

with open(my_file) as mf:
	for line in mf:
		try:
			game_info, games = line.split(":")
			games = games.replace("\n", "")
			games = games.replace(" ", "")
			games = games.split(";")
			game_number = (int)(game_info.replace("Game ", ""))
			#print(game_number, games)
			valid = True
			minblue = 0
			minred = 0
			mingreen = 0
			for game in games:
				colours = game.split(",")
				for colour in colours:
					if "blue" in colour:
						b = colour.replace("blue", "")
						b = (int)(b)
						if b > max_blue:
							valid = False
						if b > minblue:
							minblue = b
					elif "red" in colour:
						r = colour.replace("red", "")
						r = (int)(r)
						if r > max_red:
							valid = False
						if r > minred:
							minred = r
					elif "green" in colour:
						g = colour.replace("green", "")
						g = (int)(g)
						if g > max_green:
							valid = False
						if g > mingreen:
							mingreen = g
			power = minred * mingreen * minblue
			powers.append(power)
			if valid:
				valid_games += 1
				ids.append(game_number)
		except Exception as e:
			print(line)
print(f"Number of valid games: {valid_games}")
print(f"Valid game IDs: {ids}")
print(f"The sum of the valid game numbers is {np.sum(ids)}.")
print(f"Powers: {powers}")
print(f"The sum of the powers is: {np.sum(powers)}")
