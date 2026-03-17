#function to count vowels getCountOfVowel for a given string

def getCountOfVowel(string):

    #Method 1

    count=0
    if string is not None:
        for ch in string:
            if(ch=='a' or ch=='A'):
                count+=1
            elif(ch=='e' or ch=='E'):
                count+=1
            elif(ch=='i' or ch=='I'):
                count+=1
            elif(ch=='o' or ch=='O'):
                count+=1
            elif(ch=='u' or ch=='U'):
                count+=1
    print("In method 1 Number of vowels:",count)

    #Method 2

    counter=0
    vowels=['a','e','i','o','u']
    value=string.lower()
    for char in value:
        for i in vowels:
            if(char==i):
                counter+=1
    print("In method 2 Number of vowels:",counter)

input=input("Enter a string:")
getCountOfVowel(input)


