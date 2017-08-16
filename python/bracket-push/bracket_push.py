CLOSURE = {
    '{': '}',
    '[': ']',
    '(': ')'
    }

def check_brackets(text):
    stack = []
    for elem in text:
        if elem in CLOSURE.keys():
            stack.append(elem)
        if elem in CLOSURE.values():
            if not stack:
                return False
            if CLOSURE[stack[-1]] == elem:
                stack.pop()
            else:
                return False
    return not stack

