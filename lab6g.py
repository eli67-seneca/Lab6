#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-22
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6g.py

from typing import TypedDict

movies:list[dict[str, str | int]] = []

class Movie(TypedDict):
	"""
	A TypedDict for a Movie object. This is how I would prefer to handle this
	because it clearly defines the type of data in every field yet it behaves like a
	dictionary in every other way.
	"""
	name: str
	director: str
	year: int
	runtime: int	

def add_movie(name:str, director:str, year:int, runtime:int):
	# return Movie(name=name, director=director, year=year, runtime=runtime)
	movies.append({"name": name, "director": director, "year": year, "runtime": runtime})

def main():
	# Here are all the Matrix movies released to date
	add_movie("The Matrix", "The Wachowski Brothers", 1999, 136)
	add_movie("The Matrix: Reloaded", "The Wachowski Brothers", 2003, 138)
	add_movie("The Matrix: Revolutions", "The Wachowski Brothers", 2003, 129)
	add_movie("The Matrix: Revelations", "Lana Wachowski", 2021, 148)

	for m in movies:
		print(m)

if __name__ == "__main__":
	main()