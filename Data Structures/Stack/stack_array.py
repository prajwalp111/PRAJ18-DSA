stack = []

def is_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        raise IndexError("pop from empty stack")

def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        raise IndexError("peek from empty stack")


# Operations
push(stack, 10)
push(stack, 20)
push(stack, 30)

print("Stack:", stack)

print("Peek:", peek(stack))

print("Pop:", pop(stack))

push(stack, 40)

print("Peek:", peek(stack))

print("Pop:", pop(stack))
print("Pop:", pop(stack))

print("Final stack:", stack)