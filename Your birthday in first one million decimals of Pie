"""
Author: Keshav
Date: 18/11/2020
Purpose: To check whether your birth date appears in the first 1 million decimals of Pie
"""

#Also download the 'pi_dec_1m.txt' file from the repository

with open('pi_dec_1m.txt') as file:
	content = file.read()
	
possible=["1","2","3","4,","5","6","7","8","9","0"]

while True:
	birthday=input("Enter your birthday in ddmmyy format: ")
	print("Press \"q\" to quit")

	if birthday=="q":
		break
		
	if len(birthday)!=6:
		print("Please enter a valid date of birth\n")
		continue
				
	if birthday in content:
		print("Your birthday is in first 1 millionth decimals of pi\n")
	
	else:
		print("Your birthday is not there\n")
