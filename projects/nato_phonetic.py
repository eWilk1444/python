"""
Phonetic NATO alphabet using dictonaries
"""


def translate_to_nato():
    nato_alphabet = {"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet", "K": "Kilo", "L": "Lima", "M": "Mike",
                     "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Vector", "W": "Whiskey", "X": "X-Ray", "Y": "Yankee", "Z": "Zulu"}
    word_to_spell = input(
        "Please enter what you would like to translate into the NATO phonetic alphabet: ")
    word_to_spell = word_to_spell.upper()
    for letter in word_to_spell:
        print(nato_alphabet[letter])


def main():
    translate_to_nato()


main()
