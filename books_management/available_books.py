from all_books import *



category = input('''
These are the categories
a Math
b Comics
c Gaming


''')

if category == "a" or category == "math" or category == "Math" or category == "A":
    c.execute('SELECT * FROM math')
    print(c.fetchall())
    which_book = input("Which book do you want:  ")
    if which_book == " ":
        print("No spaces allowed")
    else:
        print("You have borrod " + which_book)
elif category == "b"or category == "comics" or category == "Comics" or category == "B":
    c.execute('SELECT * FROM comics')
    print(c.fetchall())
    which_book = input("Which book do you want:  ")
    if which_book == " ":
        print("No spaces allowed")
    else:
        print("You have borrod " + which_book)
elif category == "c" or category == "gaming" or category == "Gaming" or category == "C":
    c.execute('SELECT * FROM gaming')
    print(c.fetchall())
    which_book = input("Which book do you want:  ")
    if which_book == " ":
        print("No spaces allowed")
    else:
        print("You have borrod " + which_book)
else:
    print("I did not understand you. :o")
