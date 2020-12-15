'''
Author :- Keshav Kumar
Date of creation :- 15 Dec 2020
Date of posting :- 15 Dec 2020
Purpose :- To see the status of Covid-19 of any country
'''

#import covid using pip installer
from covid import Covid

covid = Covid()

cases = covid.get_status_by_country_name(input("Enter the name of the country: "))

for x in cases:
	print(f"{x} : {cases[x]}")
