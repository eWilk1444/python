"""
    Using tuples to display courses for programming certificate
"""


def main():
    """
    This function holds the tuple for the data
    and prints the tuple and its length to the terminal
    """
  programming_classes = ("Intro to Python", "Advanced Python", "Database Essentials",
                          "Web Development Basics", "Data Structures in Python", "Web Design Fundamentals")
   for course in programming_classes: # displaying all courses in order
        print(course)
    length = len(programming_classes) # finding length of tuple
    print(f"There are {
          length} courses to complete for a programming certificate. ")

# invoking main
main()
