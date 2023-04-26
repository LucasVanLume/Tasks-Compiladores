import re

OPERATORS = {'+': 'PLUS', '-': 'MINUS', '*': 'STAR', '/': 'SLASH'}

class Regex:
    @staticmethod
    def match_num(token):
        return re.match(r'\d+', token)
    
    @staticmethod
    def match_op(token):
        return re.match(r'[+\-*/]', token)

def scan(operation):
    tokens = []
    for token in operation.split():
        if Regex.match_num(token):
            tokens.append({'type': 'NUM', 'lexame': int(token)})
        elif Regex.match_op(token):
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

with open('Calc3.stk', 'r') as f:
    operation = f.read().strip()

try:
    tokens = scan(operation)
    result = rpn(tokens)
    print('Result: {}'.format(result))
    for token in tokens:
        print('Token {}'.format(token))
except ValueError as e:
    print(e)
