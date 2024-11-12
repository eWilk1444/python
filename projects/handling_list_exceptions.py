"""
Modify Artist List: Write a function to replace an artist in the top_artists list. The function should ask the user for an index and a new artist name.
    Ensure your function catches and handles ValueError for invalid number conversion and IndexError for out-of-range indices.
General Error Handling: Modify your function to catch both ValueError and IndexError using a single except block. Provide a general error message like "An input error occurred."

https://chatgpt.com/share/6732ce33-47d4-800f-97dc-1914c80f1a03 
"""


def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    # Your code goes here
    try: # error checking
        print(top_artists) # just chucking the list out there so the user can see it
        index_to_change = int(input("Enter the index of the artst to replace: ")) # get index
        artist_to_change = input("Enter the name of the artist to replace: ") # get replacement name
        top_artists[index_to_change] = artist_to_change # overwrite name in specified index
        print(top_artists) # new list printed to user
    except ValueError: # if they enter a non-integer for the index
        print("Please enter an integer. ")
    except IndexError: # if they go out of bounds in the list
        print("Please enter an index number that exists within the bounds of the list. Please select a number 0 through 9. ")
    except Exception as e: # for anything else that may happen
        print(f"An error has occurred, please try again. {e}")


main()
