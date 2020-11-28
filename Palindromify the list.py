"""
Author: Keshav
Date: 28/11/2020
Purpose: For Learning
"""

def nextPalindrome(n):
	"""Increments the value of argument by 1 if it' not a palindrome"""
	n+=1
	while not isPalindrome(n):
		n+=1		
	return n
	
def isPalindrome(n):
	"""Checks whether the given argument is palindrome or not"""
	return str(n)==str(n)[::-1]

try:	
	size=int(input("Enter the size of the list\n"))
	
except ValueError:
	print("Enter a valid input")
	exit()
	
num=[]

for i in range(size):
	try:
		num.append(int(input("Enter the element of the list\n")))
	except ValueError:
		print("Enter integers only")
		exit()
		
new_num=[]

#Appending the new values to the new list
for element in num:
	if element>10:
		new_num.append(nextPalindrome(element))
	else:
		new_num.append(element)
	
print(f"Output is : {new_num}")