# I have imported a regex library into Python#
# https://en.wikipedia.org/wiki/Regular_expression #

import re

# Calculator Title and Instruction for Quit or Stop #
print("Simplest Calculator")
print("To 'Exit' enter Quit\n")

# Assigning a Variable #
first = 0
second = True

# Used global options here#
def MathCalci():
    global second
    global first
    equation = ""
    if first == 0:
        equation = input("Enter Your Number:")
    else:
        equation = input(str(first))

    if equation == 'Quit':
        print("Bye bye Pal")
        second = False
    else:
        equation = re.sub('[a-zA-Z:,.()" "]','',equation) # Used the (re.sub) class from re library to stop printing the ...#
                                                           #.. letters and special characters inside a calculator #

        if first == 0:
            first = eval(equation)
        else:
            first = eval(str(first) + equation)

while second:
   MathCalci()
