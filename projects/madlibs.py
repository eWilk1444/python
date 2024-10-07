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
    print(f"Wake up(wake up) \
        \n{input_verb1} a {input_noun1} and put a little make-up \
        \n{input_verb2} the scars to fade away the shake-up({input_verb2} the scars to fade away the-) \
        Why'd you leave the {input_noun2} upon the table? \
        Here you go create another fable, you wanted to \
        {input_verb1} a {input_noun1} and put a little make-up, you wanted to \
        {input_verb2} the scars to fade away the shake-up, you wanted to \
        Why'd you leave the {input_noun2} upon the table? You wanted to \
        I don't think you trust \
        In my {input_adjective} {input_verb1} \
        I cry when {input_noun3} deserve to {input_verb4} \
        Wake up (wake up) \
        {input_verb1} a {input_noun1} and put a little make-up \
        {input_verb2} the scars to fade away the ({input_verb2} the scars to fade away the shake-up) \
        Why'd you leave the {input_noun2} upon the table? \
        Here you go create another fable, you wanted to \
        {input_verb1} a {input_noun1} and put a little make-up, you wanted to \
        {input_verb2} the scars to fade away the shake-up, you wanted to \
        Why'd you leave the {input_noun2} upon the table? You wanted to")


custom_song(input_verb1, input_verb2, input_verb3, input_verb4,
            input_noun1, input_noun2, input_noun3, input_adjective)
