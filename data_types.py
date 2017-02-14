#!/usr/bin/env python

# Data Types

#Immutable Data types

name = "John"  # A string Data type
user_id = 100 # Integar Data type

extra_message = """
Duck Typing (loosly typed language like perl, javascript)
Strings are immutable;
""""

name[0] = "K"  # will give an error
# how do I Change John to Kohn ?
name.replace[r'J', r'K']
# what is this r thing ? raw string

#Reverse the string ??

name[::-1]  #Splice operator
long_text = r'inventore veritatis et quasi architecto'
long_text[::-1]  # Reverse this long string
long_text[::-2]  # Reverse but print alternate words

#What is thix extra_message  - Multiline string and capable of expansion

greeting = """
Dear %s
We appreciate inquiry and your room is booked at
%s at %s City
"""  % ("John", "Taj", "Bangalore")


#-- Explore methods on string data type in ipython console

#===========
