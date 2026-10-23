#!/usr/bin/env python3
# Author: Enoch Li
# Date: 2026-10-19
# Purpose: Practice Set Operations.
# Usage: ./lab6b.py

# NOTE: For the sake of my own sanity, I will copy the optimised build_the_set() and
# test() function instead of the one I wrote to satisfy the grade requirement.

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

def s3_or_s5(s3:set[int], s5:set[int]):
	"""Returns a set containing only the elements that are unique to `s3` and `s5`.

	Args:
		s3 (set[int]): Set 3
		s5 (set[int]): Set 5
	"""
	# return s3 ^ s5
	# return s3.symmetric_difference(s5)	# Same thing
	return s3.difference(s5).union(s5.difference(s3))
	# return (s3 - s5) | (s5 - s3)  # Same thing.

def test(*args):
	sep = f"\u2014"*40
	divs = [3, 5, 7, 11] if len(args) == 0 else list(args)

	for d in divs:
		print(f"s{d}: {build_the_set(d, 0, 100)}")
		print(sep)

def main():
	buildtheSet = build_the_set
	sep = "\u2014"*40
	s3 = buildtheSet(3)
	print(f"s3:\t{s3}")
	print(sep)

	s5 = buildtheSet(5)
	print(f"s5:\t{s5}")
	print(sep)

	s3ors5 = s3_or_s5(s3, s5)
	print(f"s3^s5:\t{s3ors5}")

if __name__ == "__main__":
	main()
	# test()