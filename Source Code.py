
import re

print("Simplest Calculator")
print("To 'Exit' enter Quit\n")

first = 0
second = True

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
        equation = re.sub('[a-zA-Z:,.()" "]','',equation)

        if first == 0:
            first = eval(equation)
        else:
            first = eval(str(first) + equation)

while second:
   MathCalci()
