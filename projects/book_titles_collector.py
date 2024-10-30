"""
    Program prompts user to enter 10 book titles and then sorts them alphanumerically.
    """


def book_getter():
    """
    This function gets 10 book titles and returns them as a list

    Returns:
        str: book titles as a list
    """
    book_list = []
    while len(book_list) < 10:  # repeats until 10 book titles are given
        new_book = input("Please enter a book title: ")
        book_list.append(new_book.title())  # adds to list
    else:
        return book_list  # make book_list available in main function as the book_getter function


def main():
    """
    Creates sorted list from book_getter function and prints each item on a seperate line.
    """
    book_list = book_getter()  # grabbing book_list from book_getter
    sorted_book_list = (sorted(book_list))  # new sorted list
    for book in sorted_book_list:
        print(book)  # each item is printed on its own line


# invoking main
main()
