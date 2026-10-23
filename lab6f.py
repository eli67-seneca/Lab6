#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-22
# Purpose: Use Dictionary for Problem solving.
# Usage: ./lab5f.py

from collections import Counter

def histo_counter(in_str:str, case_sensitive:bool=False, remove_spaces:bool=False):
	"""Uses `Counter` from `collections` to print out a histogram of character frequency.

	Args:
		in_str (str): Input string
		case_sensitive (bool, optional): Case sensitivity. Defaults to False.
		remove_spaces (bool, optional): Remove spaces. Defaults to False.
	"""
	if not case_sensitive:
		in_str = in_str.casefold()
	if remove_spaces:
		in_str = in_str.replace(' ', '')
	histo = dict(Counter(in_str))
	for k, v in histo.items():
		print(f"{k} {'*'*v}")

def histogram(in_str:str):
	"""Prints out a histogram of character frequency.

	Args:
		in_str (str): Input string.
	"""
	histo = dict()
	for char in in_str.replace(' ', ''):
		if char in histo:
			histo[char] += "*"
		else:
			histo[char] = "*"

	for k, v in histo.items():
		print(f"{k} {v}")

def main():
	# histo_counter("The quick brown fox jumps over the lazy dog", case_sensitive=False, remove_spaces=True)
	# print("-"*40)
	histogram("hello amma")

if __name__ == "__main__":
	main()