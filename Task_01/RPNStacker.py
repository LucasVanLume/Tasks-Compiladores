stack = []

def push(value):
    stack.append(value)

def pop():
    return stack.pop()

def rpn(operation):
    for character in operation.split():
        if character.isdigit():
            push(int(character))
        elif character == "*":
            push(pop() * pop())
        elif character == "/":
            dig2 = pop()
            dig1 = pop()
            push(dig1 / dig2)
        elif character == "+":
            push(pop() + pop())
        elif character == "-":
            dig2 = pop()
            dig1 = pop()
            push(dig1 - dig2)
    return pop()

with open("Calc1.stk", "r") as f:
    operation = f.read().strip()

result = rpn(operation)

print(result)
print(stack)
