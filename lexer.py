import ply.lex as lex

tokens = ['ID','NUM','PLUS','MINUS','DIV','MUL','PRINT','LPAREN','RPAREN']

t_ignore =  ' \t'

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value == "exhibit":
        t.type = "PRINT"
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t



def t_error(t):
    if t.value[0] in {'@', '$', '\\'}:
        print(f"Symbol '{t.value[0]}' is not allowed")
    else:
        print(f"Unexpected character '{t.value[0]}'")
    t.lexer.skip(1)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIV = r'/'
t_MUL = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'


lexer = lex.lex()
