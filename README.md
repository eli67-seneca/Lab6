# PRG101-Lab6
### Submission Details

In this lab, you will create eight simple scripts. Write the scripts in Github codespaces. 
Write the scripts in GitHub codespaces. 
Please note that you will work on the lab during class hours and show your progress to the professor to receive the marks for the lab. If not completed, you can continue working on lab at home and submit a PDF file containing all screenshots showing your code and output in Blackboard before the due date.

### Lab Objectives

- To be able to build and use a set container.
- To be able to build and use dictionary containers.

## INVESTIGATION 1: WORKING WITH SETS

Sets are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set has similar characteristics as a list, but there are two major differences:
- Sets are un-ordered.
- Sets cannot contain duplicate values.
Set variables are created with curly brackets.

```Python
myset = {"apples", "oranges", "kiwi"}
print(myset)
# Output : {'kiwi', 'apples', 'oranges'}
```

Since new duplicate entries will be automatically ignored when adding elements to a set, they are very useful for performing tasks such as comparisons: finding similarities or differences in multiple sets. 

```Python
myset = {"apples", "oranges", "kiwi", "oranges"}
print(myset)
Output :
{'kiwi', 'apples', 'oranges'}
```
## lab6a.py
### Creating Sets
In your lab6a.py file complete the given function that creates the following four sets.
- s3 which contains numbers between 0 and 100 which are divisible by 3.
- s5 which contains numbers between 0 and 100 which are divisible by 5.
- s7 which contains numbers between 0 and 100 which are divisible by 7.
- s21 which contains numbers between 0 and 100 which are divisible by 11.
- Run the script from command line using the command: python ./lab6a.py.

### Useful Sets Functions
Set operations in Python are used to perform mathematical set operations like union, intersection, and difference. Python's set data type supports these operations directly. 

The `union` of two sets is a set containing all the elements of both sets without duplicates.

```Python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using | operator
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Using union() method
union_set_method = set1.union(set2)
print(union_set_method)  # Output: {1, 2, 3, 4, 5}
```

The `intersection` of two sets is a set containing only the elements that are common to both sets.

```Python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using & operator
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}

# Using intersection() method
intersection_set_method = set1.intersection(set2)
print(intersection_set_method)  # Output: {3}
```

The `difference` of two sets is a set containing elements that are in the first set but not in the second set.

```Python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using - operator
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}

# Using difference() method
difference_set_method = set1.difference(set2)
print(difference_set_method)  # Output: {1, 2}
```

## lab6b.py
### Set Operations

- Copy the code from lab6a.py and paste it in your lab6b.py file.
- Create a new function called `s3_or_s5()` that creates a new set of all elements that are in s3 or s5, but not both. The function should receive s3 and s5 as arguments.
- Remove extra code form main() like the calls to create s7 and s11.
- Call the function `s3_or_s5()` after the call that creates s5 and prints s5.
- Run the script from command line using the command: python ./lab6b.py.
- Take the screenshot of code showing the function `s3_or_s5()` and the output. The output must show s3, s5 and then s3ors5.
  
## lab6c.py
### Set Operations
- Copy the code from lab6b.py and paste it in your lab6c.py file.
- Create a new function called `s3_and_s5_not_s7()`that creates a new set of all elements that are in s3 and s5, but not in s7. The function should receive s3, s5 and s7 as arguments. Use the appropriate set methods (union, intersection, difference).
- Remove extra code from the main() and call the function at the appropiate location.
- Run the script from command line using the command: python ./lab6c.py.
- Take the screenshot of code showing the function `s3_and_s5_not_s7()`and the output. The output must show s3, s5, s7 and the final set elements.


## INVESTIGATION 2: DICTIONARIES

In Python, a dictionary is a set of key-value pairs. Dictionaries are unordered, like sets, however any value can be retrieved from a dictionary if you know the key. This is efficient, if you remember when working with lists, you need to access list elements through indexes; 0, 1, 2 and so forth. If you want to find some item in a list, you will either know its index, or, at worst, traverse through the entire list. In a dictionary, the items are indexed by keys. Each key maps to a value. The values stored in the dictionary can be accessed and changed using the key.

Copy the following code in a new file and run it to see the output.
```Python
this_dictionary = {}
this_dictionary["Switzerland"] = "Alps"
this_dictionary["United States"] = "Alaska Range"
this_dictionary["Armenia"] = "Caucasus"
this_dictionary["Argentina"] = "Andes"
this_dictionary["Karakoram"] = "Pakistan"

print(len(this_dictionary))
print(this_dictionary)
print(this_dictionary["Argentina"])

Output :
5
{'switzerland': 'Alps', 'United States': 'Alaska Range', 'Armenia': 'Caucasus', 'Argentina': 'Andes', 'Karakoram': 'Pakistan'}
Andes
```

The notation {} creates an empty dictionary, to which we can add content. Five key-value pairs are added:"Switzerland" maps to "Alps", "United States" maps to "Alska Rnage" and so on the rest of keys maps to their respective values. Finally, the number of key-value pairs in the dictionary is printed, along with the entire dictionary, and the value mapped to the key "Argentina".

## lab6d.py
### Working With Dictionaries

- In your lab6d.py file Create a function named `times_ten(start_index: int, end_index: int)`, which creates and returns a new dictionary.
- The keys of the dictionary should be the numbers between `start_index` and `end_index` inclusive.
- The value mapped to each key should be the key times ten.
- The function prints the exact output as:
```Python
my_dictionary = multiplyByTen(2,6)
print(my_ dictionary)
{2:20, 3:30, 4:40, 5:50, 6:60}
```
- Run the script from command line using the command: python ./lab6d.py.
- Take the screenshot of code and the output.

## lab6e.py
### Traversing a Dictionary

The familiar `for item in collection` loop can be used to traverse a dictionary, too. When used on the dictionary directly, the loop goes through the keys stored in the dictionary, one by one. 
A python dictionary can be traversed by following methods :

You can iterate through all the keys in a dictionary using a for loop.

```Python
student = {
    "name": "John Doe",
    "age": 21,
    "major": "Computer Science"
}

# Traversing keys
for key in student:
    print(key)

# Output :
name
age
major
```

To iterate through all the values in a dictionary, use the values() method.

```Python
student = {
    "name": "John Doe",
    "age": 21,
    "major": "Computer Science"
}

# Traversing values
for value in student.values():
    print(value)

Output :
John Doe
21
Computer Science
```

To iterate through key-value pairs, use the items() method, which returns a view of the dictionary’s key-value pairs as tuples.

```Python
student = {
    "name": "John Doe",
    "age": 21,
    "major": "Computer Science"
}

# Traversing key-value pairs
for key, value in student.items():
    print(f"Key: {key}, Value: {value}")

Output :
Key: name, Value: John Doe
Key: age, Value: 21
Key: major, Value: Computer Science
```

- A dictionary is provided to you in ./lab6e.py file, use the `for in` loop and `items()` methodto traverse this dictionary and print the dictionary showing the following exact output.
```Python
switzerland : Alps
United States : Alska Range
Armenia : Caucasus 
Argentina : Andes 
Karakoram : Pakistan
```
- Run the script from command line using the command: python ./lab6e.py
- Take the screenshot of code and the output.

## lab6f.py
### Using Dictionary for Problem solving

- In your lab6f.py file create a function named histogram, which takes a string as its argument.
- The function should print out a histogram representing the number of times each letter occurs in the string.
- Each occurrence of a letter should be represented by a star on the specific line for that letter.
- For example, the function call histogram("hello amma") should print :
```Python
h *
e *
l **
o *
a **
m **
```
- Use dictionary in your function and call your function histogram() from main() function. Pass any string to your histogram function.
- Run the script from command line using the command: python ./lab6f.py.

## lab6g.py
### Using Dictionary for Structured Data

Dictionaries are very useful for structuring data. For example, we can create a dictionary representing the record of each student.
```Python
Student = {"name": "Eden", "id": "eden2402", "semester": 3, "year": 2}
```
We can create multiple such records, each record representing one student. The advantage of a dictionary is that it is a collection. It collects related data under one variable, so it is easy to access the different components. 
To create a complex and more useful data structure, we can create a list of dictionaries which represent students in let’s say the course PRG101. The list represents the course and dictionary elements can be added to the list to represent the students in the course.
```Python
Student1 = {"name": "Eden", "id": "eden2402", "semester": 3, "year": 2}
Student2 = {"name": "Mustafa", "id": "mstfa12", "semester": 4, "year": 2}
Student3 = {"name": "Haiden", "id": "haiden1", "semester": 3, "year": 2}
PRG101 = [student1, Student2, Student3]
```

- In your lab6g.py file create a function named add_movie() which adds a new movie object into a movie database.
- The database is a list, and each movie object in the list is a dictionary. The dictionary should contain the following keys (name, director, year, runtime).
- The values attached to these keys should be pass as arguments to the function.
- Call the function 4 times with 4 different movies.
- In the main() function print the database with each movie data printed on a single line.
- Run the script from command line using the command: python ./lab6g.py.
- Note that this is a complex task, you are creating a list of dictionaries. It is a really useful concept and if you are able to write this script, you should be proud of you!

## lab6h.py
### Using Dictionary for Structured Data

- Copy the code from lab6g.py and paste it in lab6h.py.
- Create a new function named find_movie() which processes the movie database created in the previous exercise.
- The function should formulate a new list, which contains only the movies whose title includes the word searched for.
- Capitalization is irrelevant here. A search for "gone" should return a list containing both "Gone with the wind" and "Forever gone".
- Call the function twice with different search strings.
- Run the script from command line using the command: python ./lab6h.py.

## Lab 6 Sign-Off
- Submit the screenshots of each individual script, the screenshot must show your scripts and command line interface and output.
- The screenshot must also show your username on github codespaces.
- Submit individual screenshots of the following scripts on blackboard. If the screenshots do not correctly show the information mentioned above, you will get zero marks for the lab.
    - lab6a.py
    - lab6b.py
    - lab6c.py
    - lab6d.py
    - lab6e.py
    - lab6f.py
    - lab6g.py
    - lab6h.py

