"""
File: largest_digit.py
Name: Yudy
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	if n < 0:
		n = -n
	k = n % 10
	return find_largest_digit_helper(n, k)


def find_largest_digit_helper(n, k):
	if n % 10 == n:
		if n > k:
			k = n
		return k
	else:
		new_k = n % 10
		new_n = int((n - new_k) / 10)
		if new_k > k:
			k = new_k
		return find_largest_digit_helper(new_n, k)



if __name__ == '__main__':
	main()
