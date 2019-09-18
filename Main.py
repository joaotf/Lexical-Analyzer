import Lexical
import IDE_Lexical as ide

def main(args):
    content = ""
    with open(f"{args}",'r+') as file:
        content = file.readlines() 
    lex = Lexical.Lexical(str(content).replace("[","").replace("]","").replace("'","").replace("\\","/").replace("/n",""))
  
    tokens = lex.token();

    return tokens

    
ide.doidao1()

