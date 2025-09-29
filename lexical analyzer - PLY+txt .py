#importar PLY (PYTHON, LEX, YACC)
import ply.lex as lex
import sys

# Definición de tokens que el analizador puede reconocer
tokens = ['ID', 'NUMERO']
# Expresión regular para identificadores (variables)
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
# Expresión regular para números enteros
t_NUMERO = r'[0-9]+'
# Caracteres que serán ignorados durante el análisis
t_ignore_ESPACIO = r'[ ]+'

# Función que maneja errores léxicos
def t_error(t):
    print("Se encontró un error: %s" % repr(t.value[0]))
    t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex()

try: 
    f= open('ejemplo.txt')
    data = f.read
    f.close()
except IndexError:
    sys.stdout.write('Reading from standard input (type EOF to end):\n')
    data = sys.stdin.read

lexer.input(data)

print('Token - Lexema - Línea' )
while True: 
    tok= lexer.token()
    if not tok: break
    print('(',tok.type, ',',tok.value, ',',tok.lineno, ')')