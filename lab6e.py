#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-21
# Purpose: Traverse dictionary.
# Usage: ./lab6e.py

my_dict = {"Switzerland" : "Alps", "United States" : "Alska Range", "Armenia" : "Caucasus", "Argentina" : "Andes", "Karakoram" : "Pakistan"}

def main():
	for k, v in my_dict.items():
		print(f"{k} : {v}")

if __name__ == "__main__":
	main()