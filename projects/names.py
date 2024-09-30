"""
    This program will sort 5 user inputed names using Bubble sort
"""

# Initialize a list of numbers
peoples_names = [input("\nPlease provide a name in all lowercase. ")]

# https://chatgpt.com/share/66fb2454-2e5c-800f-9df4-5742bfe83fa1 I forgot to add the brackets to make it a list instead of a string *facepalm*

# collects all 5 names for sorting from user
while len(peoples_names) < 5:
    peoples_names.append (input("\nPlease enter another name in all lowercase. "))

# https://chatgpt.com/share/66fb2454-2e5c-800f-9df4-5742bfe83fa1 I similarily forgot how the 'not' operator works and that it would only check the list once

# Flag to track if a swap has occurred
need_swap = True

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
print(f"The sorted list of names is {peoples_names}.")
peoples_names.reverse()
print(f"The reversed list of names is {peoples_names}.")