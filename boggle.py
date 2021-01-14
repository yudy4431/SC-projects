"""
File: boggle.py
Name: Yudy
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
X_ROW = 4					# Rows the game has.
Y_COL = 4					# Columns the game has.
NUM_IN_ROW = 4				# Letters in a row.

# Global variables
dictionary = []				# Store data in FILE.
boggle_lst = []				# Store answers processed.


def main():
	read_dictionary()
	s = []													# Stores data input.
	for i in range(Y_COL):
		row = input(f'{i + 1} row of letters: ')
		string = check_format(row)							# Checks if format is right.
		s.append(string)
	print('Searching...')
	for x in range(X_ROW):
		for y in range(Y_COL):
			word = ''										# Empty word string at beginning.
			used = []										# Empty boggle answers at beginning.
			find_boggle(s, word, x, y, used)
	print(f'There are {len(boggle_lst)} words in total.')


def find_boggle(string_lst, current_word, current_x, current_y, used_position):
	"""
	Find boggle answers.
	:param string_lst: A list to store alphas input.
	:param current_word: Word gonna be checked.
	:param current_x: Current x processing.
	:param current_y: Current y processing.
	:param used_position: Store positions were processed.
	:return: Prints boggle answer.
	"""
	global boggle_lst
	# Check dictionary.
	if len(current_word) >= 4:
		if current_word in dictionary:
			if current_word not in boggle_lst:
				boggle_lst.append(current_word)
				print(f'Found: {current_word}')
				print('Searching...')

	# Recursive case.
	if has_prefix(current_word):
		# For (x, y), x and y can move -1 or 0 or 1.
		for i in range(-1, 2):
			for j in range(-1, 2):
				if (current_x+i, current_y+j) not in used_position:			# Base case.
					# Avoid the current (x, y) out of index range.
					if NUM_IN_ROW > current_x+i >= 0 and NUM_IN_ROW > current_y+j >= 0:
						# Choose. Get the current character and add current position in used_position list.
						current_word += string_lst[current_x+i][current_y+j]
						used_position.append((current_x+i, current_y+j))

						# Explore.
						find_boggle(string_lst, current_word, current_x+i, current_y+j, used_position)

						# Un-choose. Backtracks the word and pop out the position used.
						current_word = current_word[:-1]
						used_position.pop()
					else:
						pass


def check_format(input_row):
	"""
	Check if the row user input is the right format.
	:param input_row:(str) The row user input.
	:return: A string store all letters.
	"""
	lst = ''
	low = input_row.lower()

	if input_row[1] and input_row[3] and input_row[5] != ' ':
		print("Illegal input")
	else:
		if len(input_row) == 7:
			lst += low[0]+low[2]+low[4]+low[6]
			return lst
		else:
			print("Illegal input")


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary
	with open(FILE, 'r') as f:
		for line in f:
			vocab = line.split()
			dictionary.append(vocab[0])
	return dictionary


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True




if __name__ == '__main__':
	main()
