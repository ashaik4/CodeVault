# flatten 2D arrays into a single array

A = [[1, 2, 3], [4], [5, 6]]
# iterative version

def flatten_iterative(A):
    result = []
    for array in A:
        for element in array:
            result.append(element)
    return result

print(flatten_iterative(A))

