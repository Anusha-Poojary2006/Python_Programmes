#function to print ASCII values of string input

def printASCIIvalues(string):
    for character in string:
        value=ord((character))
        print(f"{character} has {value} ASCII value")

string=input("Enter a string:")
printASCIIvalues(string)
