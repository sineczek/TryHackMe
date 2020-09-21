# Intro to Python
# Data: 21.09.2020

IP:``
-----------

`print("Hello World")`

`input("Please provide your name")`

///
Operator					Syntax
Addition					+
Subtraction					-
Multiplication				*
Division					/
Modulus						%
Exponent					**
Floor Division				//

///


///
Symbol						Syntax
Greater than				>
Less than					<
Equal to 					==
Not Equal to 				!=
Greater than or equal to	>=
Less than or equal 			<=

///


///
Operator					Syntax
and 						and
OR 							or
NOT 						not
IS 							is
IN 							in

///


///
Data types 								Definition 										Example
Boolean					A value that can only be True or False.						True or False
String 				Strings are used to define text instead of numbers		"Blu3 1snt b7r0k3n - DorkStar"
Integer								Solid numbers										55
Float						Decimal numbers such as 4.6									4.6
list 			A series of different data types stored in a collection.				[1,2,3,4]
Dictionary		Similar to a list. However, Dictionaries have some interesting 		{1:"one", 2:"two", 3:"three"}
				features we will discuss as you delve deeper into this section
	

///

-------

open file: `text = open("file_name", "mode")` 

///
Mode 					Syntax 						Definition
Read 						r 					Read-only mode, cannot
												modify the file.
Write 						w 					This will write data to a file.

												Note that if the file already exists
												it will be erased!
Append						a 					This will put data at the end of a file
Special Read + Write  		r+					This mode has the ability to read and write to files
///

open_readme.py

`print(file.readline())` will print just one line