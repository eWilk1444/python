"""
    Define a generator function two_letter_combinations that takes a list of characters as an argument.
Use nested loops within the generator function to iterate over the list of characters.
    In each iteration, concatenate two characters and use the yield statement to yield the two-letter combination.
In the main method, call the generator function with a list of characters and iterate over the generator to print each combination. 
    Create an original  5-letter list.
Include comments in your code to explain the logic behind the generator function and the use of the yield statement.
    """

# get current letter, then add next letter until end of list, then move on to next letter, aa ab ac ba bb bc etc.


def two_letter_combinations(letter_list):
    # for each letter in the letter_list
    for first_letter in letter_list:
        # for each letter in the letter_list
        for second_letter in letter_list:
            # concatenate both together
            yield first_letter + second_letter


def main():
    letter_list = ["h", "i", "j", "k", "l"]
    result = list(two_letter_combinations(letter_list))
    print(result)


main()
