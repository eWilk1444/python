"""
    This program will sort 5 user inputed names using Bubble sort
"""

# Initialize a list of numbers
peoples_names = str(input("\nPlease provide a name in all lowercase. "))

# collects all 5 names for sorting from user
if len(peoples_names) < 5:
    peoples_names = str(input("\nPlease enter another name in all lowercase. "))

# Flag to track if a swap has occurred
need_swap = bool(True)

# Continue looping until no swaps occur
while need_swap:
    need_swap = False  # Reset the flag at the start of each iteration
    for i in range(len(peoples_names) - 1):
        # Compare adjacent elements
        if peoples_names[i] > peoples_names[i + 1]:
            need_swap = True  # A swap is needed
            # Swap the elements
            peoples_names[i], peoples_names[i + 1] = peoples_names[i + 1], peoples_names[i]

# Print the sorted list
print(peoples_names)
