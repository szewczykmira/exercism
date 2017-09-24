import ast
import operator

class Parser:
    PLUS = ['plus', '+']
    MINUS = ['minus', '-']
    MULTIPLY = ['multiplied by', '*']
    DIVIDED = ['divided by', '/']
    BEGINNING = ['What is', '']
    END = ['?', '']
    OPERATIONS = [PLUS, MINUS, MULTIPLY, DIVIDED, BEGINNING, END]

    def validate_text(self, text):
        if not (text.startswith('What is ') and text.endswith('?')):
            raise ValueError

    def parse(self, text):
        self.validate_text(text)
        for operation in self.OPERATIONS:
            text = text.replace(*operation)
        return text.strip()


class Interpreter:
    OPS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv
    }

    def ast_eval(self, text):
        node = ast.parse(text, mode='eval')
        def _eval(node):
            if isinstance(node, ast.Expression):
                return _eval(node.body)
            elif isinstance(node, ast.Str):
                return node.s
            elif isinstance(node, ast.Num):
                return node.n
            elif isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
                operand = _eval(node.operand)
                if isinstance(operand, ast._NUM_TYPES):
                    if isinstance(node.op, ast.UAdd):
                        return +operand
                    else:
                        return -operand
            elif isinstance(node, ast.BinOp):
                return self.OPS[type(node.op)](_eval(node.left), _eval(node.right))
            else:
                raise ValueError

        return _eval(node.body)


def calculate(text):
    # FYI - first multiply then add!
    text = Parser().parse(text)
    try:
        return Interpreter().ast_eval(text)
    except SyntaxError:
        raise ValueError
