import re
from lexer import lexer
from parser import parser


def read_code(filename):
    with open(filename,'r') as file:
        return file.read()


def remove_comments(code):
    pattern = r'(?<!#[^\'"])(#.*?$)'
    cleaned_code = re.sub(pattern, '', code, flags=re.MULTILINE)
    return cleaned_code



# def process_code(code):
#     clean_code = remove_comments(code)
#     lines = clean_code.split('\n') 
#     lines = [line.strip() for line in lines] 
#     lines = [line for line in lines if line]  #remove empty line
#     return lines


def get_clean_code(code):
    code = remove_comments(code)

    return code
    

# def get_tokens(code):
#     lexer.input(code) 
#     tokens = []
    
#     while True:
#         tok = lexer.token()  
#         if not tok:
#             break  
#         tokens.append({
#             'type': tok.type,
#             'value': tok.value,
#             'line': tok.lineno,  
#             'position': tok.lexpos  
#         })
    
#     return tokens

def main():
    filename = "/home/kali/Documents/Password Manager/ProgrammingLanguageForEnglishMajors/test.plem"
    code = read_code(filename)
    code = get_clean_code(code)
    lexer.input(code)
    result = parser.parse(code)
    print(result)










if __name__ == "__main__":
    main()