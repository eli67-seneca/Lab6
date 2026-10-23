#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-20
# Purpose: Creating dictionary.
# Usage: ./lab6d.py

def times_ten(start_index:int, end_index:int) -> dict[int, int]:
	"""Returns a dictionary containing keys corresponding to all the numbers
	between `start_index` and `end_index` inclusively and values that are the keys
	times ten.

	Args:
		start_index (int): Starting value
		end_index (int): Ending value (inclusive)

	Returns:
		dict[int, int]: Dictionary containing the key's value times ten as its mapped value.
	"""
	return {n: n*10 for n in range(start_index, end_index + 1)}

def main() -> None:
	multiplyByTen = times_ten
	my_dictionary = multiplyByTen(2, 6)
	print(str(my_dictionary).replace(': ', ':'))

if __name__ == "__main__":
	main()