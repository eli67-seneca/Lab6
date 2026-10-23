#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-20
# Purpose: Create Sets.
# Usage: ./lab6a.py

def buildtheSet(divisor:int) -> set:
	"""Returns the set of numbers divisible by `divisor` from 0 to 100.

	Args:
		divisor (int): Number to divide by

	Returns:
		set: A set of numbers divisible by `divisor` from 0 to 100
	"""
	# return build_the_set(divisor, 0, 100, False)
	s = set()
	for i in range(0, 101):
		if i % divisor == 0:
			s.add(i)
	return s

def build_the_set(divisor:int, start:int=0, stop:int=100) -> set:
	"""A more comprehensive implementation of `buildTheSet()`.\n
	Returns the set of numbers divisible by `divisor`, inclusively from `start`
	to `stop`, and optionally sorted.

	Args:
		divisor (int): Number to be divided
		start (int, optional): Starting value. Defaults to 0.
		stop (int, optional): Stopping value. Defaults to 100.

	Returns:
		set: A set of numbers divisible by `divisor`.
	"""
	return {i for i in range(start, stop + 1) if i % divisor == 0}

def test(*args):
	sep = f"\u2014"*40
	divs = [3, 5, 7, 11] if len(args) == 0 else list(args)

	for d in divs:
		print(f"s{d}: {build_the_set(d, 0, 100)}")
		print(sep)

def main():
	# sep = "-"*40
	s3 = buildtheSet(3)
	print("s3: ", s3)
	print("----------------------------------------")

	s5 = buildtheSet(5)
	print("s5: ", s5)
	print("----------------------------------------")

	s7 = buildtheSet(7)
	print("s7: ", s7)
	print("----------------------------------------")

	s11 = buildtheSet(11)
	print("s11: ", s11)

if __name__ == "__main__":
	main()
	# test()