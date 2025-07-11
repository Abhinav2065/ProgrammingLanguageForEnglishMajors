import ply.yacc as yacc
from lexer import tokens, lexer


def p_assignment(p):
    p[0] = ('ASSIGN', p[1], p[3])


def p_binop(p):
    p[0] = ('BINOP', p[2], p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('NUMBER', p[1])

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Build 
parser = yacc.yacc()