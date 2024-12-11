def isInteger(string):
    
    if len(string) == 0:
        return False
    
    for i in range(len(string)):
        if string[i] != ' ':
            string = string[i:]
            break

    if string[0] in "+-&":
        if len(string) > 1 and all(char in "0123456789" for char in string[1:]):
            return True
        else:
            return False
    
    if all(char in "0123456789" for char in string):
        return True
    
    return False

print(isInteger("123")) 
print(isInteger("   456   ")) 
print(isInteger("  -789  ")) 
print(isInteger("-12ab"))
print(isInteger("0"))