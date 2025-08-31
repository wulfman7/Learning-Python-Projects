from mistune.plugins.table import ALIGN_CENTER

print()
print("\033[1mHello, World! Time to learn different formatting in Python!\033[0m")
print()
print("This creates\na new line")          # \n creates a |New line|
print()
print()
print("Column 1\tColumn 2")      # \t creates a |Tab space|
print()
print("The last character was just deletedd\b")            # \b creates a |Backspace (deletes last character)|
print()
print("This is a quote: \"To be or not to be\"")    # \" \" creates an |Escaped double quote|
print()
print("\\")                     # \\ creates a |Backslash|
print()
print("Hello", "to those", "here" , "and" , "everywhere", sep="---")        # sep="(insert here)" creates a |replacement for commas|
print()
print("Hello", end="!!!\n")      # end="(insert here)" creates an |ending instead of a default new line|
print("\n\n\n")

# \033[ starts an ANSI code    -   Enclose in ("\033[__m   insert text here    \033[0m")
# 1m = bold
# 4m = underline
# 30–37m = text colors
# 0m resets formatting

print("\033[1mBold Text\033[0m")
print("\033[4mUnderlined Text\033[0m")
print("\033[31mRed Text\033[0m")
print("\033[32mGreen Text\033[0m")
print("\033[33mYellow Text\033[0m")
print("\033[34mBlue Text\033[0m")
print()

print("""This is
a block
of text""")                     # Extra " makes for |Multiline|

print()
name = "Alice"                  # Define variable "name"
age = 25                        # Define variable "age"
print(f"My name is {name} and I am {age} years old")        # f before " allows for |insertion of variables in print|
print(f"{name} was looking forward to her {age}th birthday")
print()
print()
print()
print()                         # print() creates a |simple new line|
