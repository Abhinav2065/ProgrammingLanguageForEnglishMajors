from ply import lex
import re


def read_code(filename):
    with open(filename,'r') as file:
        return file.read()


def remove_comments(code):
    pattern = r'(?<!#[^\'"])(#.*?$)'
    cleaned_code = re.sub(pattern, '', code, flags=re.MULTILINE)
    return cleaned_code



def process_code(code):
    clean_code = remove_comments(code)
    lines = clean_code.split('\n') 
    lines = [line.strip() for line in lines] 
    lines = [line for line in lines if line]  #remove empty line
    return lines



#Tokens
tokens = ["NUMBERS","PLUS","MINUS","MUL","DIV","LPAREN","RPAREN"]
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_MUL    = r'\*'
t_DIV    = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = ' \t'


