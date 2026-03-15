#function to getStrlength to get string length

def getStrlength(string):

    # first method
    if string!=None:
        number=len(string)
        print(f"In first method length of string {string} is {number}")

    #second method
    count=0
    if string!=None:
        for character in string:
            count+=1
    print(f"In second method length of string {string} is {count}")

string=None
getStrlength(string)
