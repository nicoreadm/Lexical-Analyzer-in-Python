import re


class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.token_specification = [
            ('PRINT',   r'print\b'),
            ('QUOTATION',   r'\"'),
            ('COMMA',   r','),
            ('SEMICOLON',   r';'),
            ('DOT',   r'\.'),
            ('COLON',   r':'),
            ('EQUALS',   r'=='),
            ('NOT_EQUALS',   r'!='),
            ('GREATER_THAN',   r'>'),
            ('LESS_THAN',   r'<'),
            ('GREATER_THAN_OR_EQUALS',   r'>='),
            ('LESS_THAN_OR_EQUALS',   r'<='),
            ('AND',   r'and'),
            ('INPUT',   r'input\b'),
            ('NUMBER',   r'\d+'),
            ('PLUS',     r'\+'),
            ('MINUS',    r'-'),
            ('MULTIPLY',    r'\*'),
            ('ASSIGN',   r'='),
            ('LPAREN',  r'\('),
            ('RPAREN',  r'\)'),
            ('STRING',  r'"[^"\n]*"'),
            ('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),
            ('SKIP',     r'[ \t]+'),
            ('NEWLINE',  r'\n'),
            ('MISMATCH', r'.'),
        ]
        self.tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.token_specification)

    def tokenize(self):
        for mo in re.finditer(self.tok_regex, self.text):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'NUMBER':
                value = int(value)
                self.tokens.append(Token('NUMBER', value))
            elif kind == 'PRINT':
                self.tokens.append(Token('PRINT', value))
            elif kind == 'QUOTATION':
                self.tokens.append(Token('QUOTATION', value))
            elif kind == 'INPUT':
                self.tokens.append(Token('INPUT', value))
            elif kind == 'PLUS':
                self.tokens.append(Token('PLUS', value))
            elif kind == 'MINUS':
                self.tokens.append(Token('MINUS', value))
            elif kind == 'MULTIPLY':
                self.tokens.append(Token('MULTIPLY', value))
            elif kind == 'ASSIGN':
                self.tokens.append(Token('ASSIGN', value))
            elif kind == 'LPAREN':
                self.tokens.append(Token('LPAREN', value))
            elif kind == 'RPAREN':
                self.tokens.append(Token('RPAREN', value))
            elif kind == 'STRING':
                self.tokens.append(Token('STRING', value))
            elif kind == 'ID':
                self.tokens.append(Token('ID', value))
            elif kind == 'NEWLINE' or kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'Unexpected character: {value}')
        return self.tokens


codigo = str(input("ingrese el codigo: "))
lexer = Lexer(codigo)
print(lexer.tokenize())

