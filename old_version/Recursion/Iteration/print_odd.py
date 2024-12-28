# code to print elements at odd indices of an array
def printOdd(A):
    def printOddRecursive(A, i):
        if i == len(A):
            return
        if i % 2 != 0:
            print(A[i])
        printOddRecursive(A,i+1)
    return printOddRecursive(A, 0)
A = [2,4,6,8,10,12]
print(printOdd(A))