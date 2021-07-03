# insert at the bottom of a stack iteratively

def insertAtBottomIterative(stack, element):
    temp_stack = list()
    while stack:
        temp_stack.append(stack.pop())
    stack.append(element)
    while temp_stack:
        stack.append(temp_stack.pop())
    return stack
stack = [2,3,4,5,6,7,8]
element = "element"

print(insertAtBottomIterative(stack, element))


def insertAtBottomRecursive(stack, element):
    if len(stack) <= 0:
        stack.append(element)
        return
    temp = stack.pop()
    insertAtBottomIterative(stack, element)
    stack.append(temp)
    return stack

stack = [2,3,4,5,6,7,8]
element = "element"
print(insertAtBottomRecursive(stack, element))
