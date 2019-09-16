import Lexical
import IDE_Lexical as ide

def main(args):
    content = ""
    with open(f"{args}",'r+') as file:
        content = file.read()
    
    lex = Lexical.Lexical(content)
    tokens = lex.token();

    return tokens

    
ide.doidao1()

