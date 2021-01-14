"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variables
dictionary = []


def main():
	read_dictionary()
	row1 = input('1 row of letters: ')
	s1 = check_format(row1)
	row2 = input('2 row of letters: ')
	s2 = check_format(row2)
	row3 = input('3 row of letters: ')
	s3 = check_format(row3)
	row4 = input('4 row of letters: ')
	s4 = check_format(row4)
	s = ''
	s += s1+s2+s3+s4
	print(s)
	find_boggle(s)


def find_boggle(total_string):
	global dictionary
	current_index = ''
	boggle_lst = []
	if len(current_index) >= 4:
		current_word = ''
		for i in range(len(current_index)):
			current_word += total_string[int(current_index[i])]
		if current_word in dictionary:
			if current_word not in boggle_lst:
				boggle_lst.append(boggle_lst)
				print(current_word)
				print(boggle_lst)
	else:
		for i in range(len(total_string)):
			if str(i) not in current_index:
				current_index += str(i)
				if i+1 % 4 == i % 4:
					current_index += str(i+1)
				elif i+1 % 4 == (i % 4) + 1 or i+1 % 4 == (i % 4) - 1:
					current_index += str(i + 1)
				else:
					find_boggle(current_index)
					current_index = current_index[:len(current_index) - 1]


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
	pass


def test():
	lst = [1, 4, 2, 3]
	n = len(lst)
	for i in range(n):
		for j in range(0, n-i-1):
			if lst[j] > lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]

	print(lst)



if __name__ == '__main__':
	main()
