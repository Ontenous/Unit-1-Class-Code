"""
Name: William Nathan
Date: 9-16-24
Description: Unit 2 Lesson 1 Notes

"""

# Variables - store information

message = "Hello, User" #string variable
print(message)

# snake_case to name our variables
user_name = input("Enter your name: ")
user_id = int(input("Enter your id: "))

# variable type command
# print(type(user_name))

# Type 1 - Strings
# can use ' or " to indicate string - be consistent

# f-strings are formatted strings that help with combining string

# Way 1 to combine string: use + (concatenation)
# Caution: all numbers require str( ) around them
message_one = "Welcome " + user_name + " with ID " + str(user_id)
print(message_one)

# Way 2 - use f strings
message_two = f"Welcome {user_name} with ID {user_id}"
print(message_two)

# Possible errors
# apostrophes inside of single quotes
# resolution: use escape sequence \ - tells python next symbol is literally that thing, no pythonic meaning
famous_quotation = "Quotations are hard to find in the middle of lessons - it\'s annoying. Mr. Smith"

# raw strings
cat = r""" 
_._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-"""

print(cat)