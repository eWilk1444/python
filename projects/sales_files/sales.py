"""
Open the file sales_totals in read mode (Download: sales_totals.txt Download sales_totals.txt)
Read in all the lines using a loop
Strip the newline symbol and convert each line to a float
Add each number to the running total
Count the number of lines
Format and display each number
Outside of the loop, format and display the total, the count, and the average
Do this using a main function 
Use try and except statements to handle file errors
"""


def main():

    with open('C:/Users/ewilkening/Desktop/python/projects/sales_files/sales_totals.txt', 'r') as file:
        line = file.readline()
        while line:
            line = file.readline()
            print(line, end="")


main()
