OPERATORS = {'+': 'PLUS', '-': 'MINUS', '*': 'STAR', '/': 'SLASH'}

def scan(operation):
    tokens = []
    for token in operation.split():
        if token.isdigit():
            tokens.append({'type': 'NUM', 'lexame': int(token)})
        elif token in OPERATORS:
            tokens.append({'type': OPERATORS[token], 'lexame': token})
        else:
            raise ValueError('Unexpected character: {}'.format(token))
    return tokens

def push(stack, value):
    stack.append(value)

def pop(stack):
    return stack.pop()

def rpn(tokens):
    stack = []
    for token in tokens:
        if token['type'] == 'NUM':
            push(stack, token['lexame'])
        elif token['type'] == 'PLUS':
            push(stack, pop(stack) + pop(stack))
        elif token['type'] == 'MINUS':
            dig2 = pop(stack)
            dig1 = pop(stack)
            push(stack, dig1 - dig2)
        elif token['type'] == 'STAR':
            push(stack, pop(stack) * pop(stack))
        elif token['type'] == 'SLASH':
            dig2 = pop(stack)
            dig1 = pop(stack)
            push(stack, dig1 / dig2)
    return pop(stack)

with open('Calc2.stk', 'r') as f:
    operation = f.read().strip()

try:
    tokens = scan(operation)
    result = rpn(tokens)
    print('Result: {}'.format(result))
    for token in tokens:
        print('Token {}'.format(token))
except ValueError as e:
    print(e)
