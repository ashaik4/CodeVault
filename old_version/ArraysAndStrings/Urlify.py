"""
1.3: Write a method to replace all spaces in a string with %20. You may assume that the string has sufficient
space at the end to hold the additional characters, and that you are given the "true" length of the string.
e.g: input: "Mr John Smith    ", 13
output = "Mr%20John%20Smith"
"""
"""
[M,r, ,J,o,h,n, ,S,m,i,t,h, , , , ,]
[M,r, ,J,o,h,h, ,S,m,i,t,S,m,i,t,h]
[M,r,%,2,0,J,o,h,n,%,2,0,S,m,i,t,h]
"""
def urlify(string, truelength):
    charArr = list(string)
    pointer = len(charArr) - 1
    for i in range(truelength - 1, - 1, - 1):
        if charArr[i] != ' ':
            charArr[pointer] = charArr[i]
            pointer -= 1
        else:
            charArr[pointer] = '0'
            charArr[pointer - 1] = '2'
            charArr[pointer - 2] = '%'
            pointer -= 3
    return "".join(charArr)


string = "Mr John Smith    "
tl = 13
print(urlify(string, tl ))
