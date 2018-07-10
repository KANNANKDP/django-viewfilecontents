#1. Write a Python program to check that a string contains only a-z, A-Z and 0-9

import re

user_str = raw_input("Enter a string to check whether it contains only a-z, A-Z and 0-9 : ")

strObj = re.search(r'[a-z][A-Z][0-9]*',user_str,re.I | re.M)

if strObj:
	print("The string is validated and it's OK")

else:
	print("The string has failed the validation")

