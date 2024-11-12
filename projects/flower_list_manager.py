"""
Manage a list of flowers. This includes sorting the list, searching for specific flowers, and handling exceptions using try and except statements.

Create a Main Function: Encapsulate your program within a main() function.
User Input for Flower List: Prompt the user to enter names of flowers and store them in a list. Have them enter the word "done" when done, and check for it.
Sorting and Searching: Sort the list, print on screen with a number next to the flower name, and allow the user to search for a specific flower. Print a message if the flower is found.
Accessing a Specific Flower: Ask the user for a number to access the corresponding flower. Handle errors for invalid inputs. (Note, our printout starts at 1, list indexes start at 0, adjust accordingly.
Exception Handling: Use try and except statements for ValueError and IndexError, and include a generic except statement.
Upload to GitHub: Upload your completed script to your GitHub repository.
Submission: Submit the GitHub repository link containing your script.

Credit for what enumerate does: https://stackoverflow.com/questions/364621/how-to-get-items-position-in-a-list
https://chatgpt.com/share/6732c7a1-599c-800f-a952-6954272a09f0 
"""


def flower_list_input():
    # gets flower names from user and puts them in a list
    try:
        flower_list = []
        flower = input("Please enter the name of a flower: ")
        while flower != "done":
            flower_list.append(flower)
            flower = input("Please enter the name of another flower, or enter 'done' if finished: ")
        return flower_list
    except Exception as e:
        print(f"Oops, something went wrong. {e}") # I cannot think of any specific errors that could occur with this because everything turns into a string, and strings can have anything in them without exploding.


def main():
    # main logic
    flower_list = flower_list_input()
    flower_list.sort()
    
    for flower_index, flower_name in enumerate(flower_list): # index = index of the flower, item = flower name
        print(f"{flower_index + 1} {flower_name}")
    
    try:
        flower_to_check = input("Please enter the name of the flower you wish to find: ")

    # setting flag for comparison of user requested flower name to names in list
        is_flower = False
        for flower_name in flower_list:
            if flower_name == flower_to_check:
                is_flower = True
                break # when finding the first instance of the flower, stop loop
        if is_flower:
            print(f"The flower {flower_to_check} is in the list is at spot number {flower_list.index(flower_to_check) + 1}.")
        else:
            print(f"{flower_to_check} is not in the list.")
    except ValueError:
        print("Oops, please enter the name of the flower you want to find.")
    except IndexError:
        print("Whoops, that spot doesn't exist in the list!")


# invoking main
main()
