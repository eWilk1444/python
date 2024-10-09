"""
    It's madlibs, iykyk
"""

input_verb1 = input("Enter a verb: ")
input_verb2 = input("Enter another verb: ")
input_verb3 = input("Enter another verb: ")
input_verb4 = input("Enter a final verb: ")
input_noun1 = input("Enter a noun or name: ")
input_noun2 = input("Enter another noun or name: ")
input_noun3 = input("Enter a final noun or name: ")
input_adjective = input("Enter an adjective: ")


# Opening chorus of 'Chop Suey' by System of a Down
def custom_song(input_verb1, input_verb2, input_verb3, input_verb4, input_noun1, input_noun2, input_noun3, input_adjective):
    """Substitutes words in Chop Suey with user entered words

    Args:
        input_verb1 - input_verb4(str): user entered verbs
        input_noun1 - input_verb3(str): user entered nouns
        input_adjective (str): user entered adjective
    """
    print(f"Wake up(wake up) \
        \n{input_verb1} a {input_noun1} and put a little make-up \
        \n{input_verb2} the scars to fade away the shake-up({input_verb2} the scars to fade away the-) \
        \nWhy'd you leave the {input_noun2} upon the table? \
        \nHere you go create another fable, you wanted to \
        \n{input_verb1} a {input_noun1} and put a little make-up, you wanted to \
        \n{input_verb2} the scars to fade away the shake-up, you wanted to \
        \nWhy'd you leave the {input_noun2} upon the table? You wanted to \
        \nI don't think you trust \
        \nIn my {input_adjective} {input_verb1} \
        \nI cry when {input_noun3} deserve to {input_verb4} \
        \nWake up (wake up) \
        \n{input_verb1} a {input_noun1} and put a little make-up \
        \n{input_verb2} the scars to fade away the ({input_verb2} the scars to fade away the shake-up) \
        \nWhy'd you leave the {input_noun2} upon the table? \
        \nHere you go create another fable, you wanted to \
        \n{input_verb1} a {input_noun1} and put a little make-up, you wanted to \
        \n{input_verb2} the scars to fade away the shake-up, you wanted to \
        \nWhy'd you leave the {input_noun2} upon the table? You wanted to")

# invoking function
custom_song(input_verb1, input_verb2, input_verb3, input_verb4,
            input_noun1, input_noun2, input_noun3, input_adjective)
