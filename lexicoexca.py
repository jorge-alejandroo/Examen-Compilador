import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMBER', 'DECIMAL', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN'
)

# Reglas de los tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# Definir regla para números decimales
def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)  # Convertir a tipo float
    return t

# Definir regla para números enteros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Función para tokenizar
def tokenize(expression):
    lexer.input(expression)
    tokens = []
    for tok in lexer:
        token_type = None
        if tok.type == 'NUMBER':
            token_type = "Número entero"
        elif tok.type == 'DECIMAL':
            token_type = "Número decimal"
        elif tok.type == 'PLUS':
            token_type = "Operador suma"
        elif tok.type == 'MINUS':
            token_type = "Operador resta"
        elif tok.type == 'TIMES':
            token_type = "Operador multiplicación"
        elif tok.type == 'DIVIDE':
            token_type = "Operador división"
        elif tok.type == 'LPAREN':
            token_type = "Paréntesis izquierdo"
        elif tok.type == 'RPAREN':
            token_type = "Paréntesis derecho"
        
        tokens.append({"token": tok.value, "type": token_type})
    return tokens

