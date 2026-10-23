#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-22
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6h.py

# NOTE: I'm going to use my unused Movies TypedDict from the previous lab
# because it's so much cleaner and makes my type checker happier.

from typing import TypedDict

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

movies:list[Movie] = []

def add_movie(name:str, director:str, year:int, runtime:int):
	m = Movie(name=name, director=director, year=year, runtime=runtime)
	movies.append(m)

def find_movie(search_terms:str) -> list[Movie]:
	"""Finds a movie in `movies` by title

	Args:
		search_terms (str): Search terms.

	Returns:
		list[Movie]: A list of movies in `movies`, if any.
	"""
	results = []
	for m in movies:
		if search_terms.casefold() in m.get('name').casefold():
			results.append(m)

	return results

def main():
	sep = "\u2014"*40
	# All the Matrix movies released to date
	add_movie("The Matrix", "The Wachowski Brothers", 1999, 136)
	add_movie("The Matrix: Reloaded", "The Wachowski Brothers", 2003, 138)
	add_movie("The Matrix: Revolutions", "The Wachowski Brothers", 2003, 129)
	add_movie("The Matrix: Revelations", "Lana Wachowski", 2021, 148)

	# for m in movies:
	# 	print(m)

	print("Search term: 'Matrix'")	# Returns all four movies
	print(*find_movie("Matrix"), sep='\n')
	print(sep)

	print("Search term: 'x: R'")	# Returns only the sequels, all of which start with R
	print(*find_movie("x: R"), sep='\n')
	print(sep)

if __name__ == "__main__":
	main()