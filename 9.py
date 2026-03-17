#Function to reverse string reverseString

def reverseString(string):

    # Method 1
    print(string[::-1])

    # Method2
    n=len(string)
    reverse=""
    for i in range(n-1,-1,-1):
        reverse+=string[i]
    return reverse

    
input='hello'      
val=reverseString(input)
print(val)

