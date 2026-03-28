#function to find given string is Palindrome,function isPalindrome returns true if string is palindrome

def isPalindrome(string):
    
    #Method 1
    if(string==string[::-1]):
        return True
    else:
        return False


    #Method 2
    leftIndex=0
    rightIndex=len(string)-1
    result=True
    while (leftIndex<rightIndex):
        if (string[leftIndex]!=string[rightIndex]):
            result=False
            break
        leftIndex+=1
        rightIndex-=1
    return result
    


input=input("Enter a string:")
condition=isPalindrome(input)

if(condition):
    print("String is a palindrome ")
else:
    print("String is not a palindrome")