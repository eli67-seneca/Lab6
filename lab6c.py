#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-20
# Purpose: Practice Set Operations.
# Usage: ./lab6c.py

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

def test(*args) -> None:
	sep = f"\u2014"*40
	divs = [3, 5, 7, 11] if len(args) == 0 else list(args)

	for d in divs:
		print(f"s{d}: {build_the_set(d, 0, 100)}")
		print(sep)

def s3_and_s5_not_s7(s3:set[int], s5:set[int], s7:set[int]):
	# return s3 & s5 - s7
	return s3.intersection(s5).difference(s7)

def main():
	buildtheSet = build_the_set
	sep = "\u2014"*40
	s3 = buildtheSet(3)
	print(f"s3:\n{s3}")
	print(sep)

	s5 = buildtheSet(5)
	print(f"s5:\n{s5}")
	print(sep)

	s7 = buildtheSet(7)
	print(f"s7:\n{s7}")
	print(sep)

	s3s5s7 = s3_and_s5_not_s7(s3, s5, s7)
	print(f"s3 and s5 not s7:\n{s3s5s7}")
	print(sep)

if __name__ == "__main__":
	main()
