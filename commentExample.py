# commentExample.py
# Purpose: This file is to provide an example of the quality 
# and format of commenting on files. There will be a header 
# at the top that contains a general description of the 
# file purpose along with information about the author.
# Author: Troy Schotter
# Recieved Help From: Coffee


# calcAge(currentYear, yearBorn)
# parameters:
#   currentYear: integer representing a specific year
#   yearBorn: integer representing a specific year
# returns:
#   x: a calculated integer that represents an estimated age
# purpose:
# This function takes a two years and calculates the age at
# at the end of the "currentYear", returning that integer value 
def calcAge(currentYear, yearBorn):
    x = currentYear - yearBorn
    return x



# main()
# parameters: none
# return: none
# purpose:
# This extremely complex function runs when the program runs
# and acts as the starting point of the file. 
# says "Hello World" and the age of Troy at the end of 2026.
def main():
    print("Hello World")
    print(f"I will be {calcAge(2026, 1989)} this year")

if __name__ == "__main__":
    main()