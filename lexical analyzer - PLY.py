#importar PLY (PYTHON, LEX, YACC)
import ply.lex as lex

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

# Solicitar entrada del usuario
data=input('Ingrese cadena: ')
# Proporcionar la cadena al analizador
lexer.input(data)

# Mostrar encabezado de resultados
print('Token - Lexema')
# Procesar todos los tokens
while True:
    tok = lexer.token()
    if not tok: break
    print('(',tok.type, ',',tok.value,')')