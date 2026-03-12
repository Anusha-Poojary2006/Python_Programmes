# function isDegit isNumber to return true if it is a digit

def isDigit(value):
    flag=True
    for eachcharacter in value:
        if(eachcharacter>='0' and eachcharacter<='9'):
            continue
        else:
            flag=False
            break
    return flag
result=isDigit('1234')
if result:
    print("It is a integer ")
else:
    print("it is not a integer")