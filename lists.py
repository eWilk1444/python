"""
    Examples of lists and their uses in a file.
"""
# ducks and stuff

# my_list = [1, 2, 3]
# my_list.append(2)
# print(my_list)
# my_list.remove(2)
# print(my_list)
# my_list.sort()
# print(my_list)

# # grabs last by default
# my_list.pop()
# print(my_list)

# print(len(my_list))

my_list1 = ["1", "2", "3", "A", "B", "C", "a", "b", "c"]
# my_list1.sort()
# print(my_list1)

# my_list1.append(3)
# print(my_list1)

# my_list1.remove(3)
# print(my_list1)

# my_list1.reverse()
# print(my_list1)

# my_list1.sort()
# print(my_list1)

# my_list1.reverse()
# print(my_list1)

# popped = my_list1.pop(0)
# print(my_list1)
# print(popped)

# print(len(my_list1))

# for item in my_list1:
#     print(item)

# # List of months in a year
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
# Corresponding list of the number of days in each month
# # Note: This list ignores leap years for February
num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Iterate through each month using a for loop for i in range(len(months)):
# Retrieve the month name from the months list

for i in range(len(months)):
    month = months[i]
    # Retrieve the number of days from the num_of_days list
    days = num_of_days[i]
    # Print the month and its corresponding number of days
    # using the f formatting prevents a problem from concatenating the num_of_days which are integers into the string
    print(f"{month} has {days} days")
    # This loop steps through each index from 0 to 11 (for 12 months)
    # and uses the index to access elements from both lists.
