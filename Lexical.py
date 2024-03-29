import re

reservadas = [
    "int",
    "double",
    "if",
    "else",
    "while",
    "for",
    "print",
    "read"
]

agrupadores = [
    "(",
    ")",
    "[",
    "]",
    "{",
    "}"
]

comparadores = [
    ">",
    "<",
    "=="
]

class Lexical(object):
    def __init__(self, source_code):
        self.source_code = source_code


    def token(self):
    
        tokens = []

        source_code = self.source_code.split()

        source_index = 0

        while (source_index < len(source_code)):
            word = source_code[source_index]
            

            for i in reservadas:
                if(re.match(f"({i})+",word) != None):
                    print(i)
                    tokens.append(f"Token (Palavra Reservada) : {word}")
            
            if(re.match("\W+",word) == None):
                if(re.match(r"[a-z|A-Z]+[0-9]+|[a-z|A-Z]+",word) and word not in reservadas):
                    tokens.append(f"Token (Identificador) : {word}")
            
            if(re.match(r"[$%¨¨&*!§]+",word)):
                tokens.append(f"Token não identificado : {word}")

            elif(re.match(r"(\d+\.\d+)",word)):
                tokens.append(f"Token (Double) : {word}")

            elif(re.match(r'(\d+)', word)):
                tokens.append(f"Token (Inteiro) : {word}")

            elif(re.match("\#",word)):
                tokens.append(f"Token (Comentário) : {word}")   

            if(re.match("(=)",word)):
                if(word.count("=") == 1):
                    tokens.append(f"Token (Atribuição) : {word}")
            
            elif(re.match("\(",word)):
                tokens.append(f"Token (Agrupadores) : {word}")
                 
            elif(re.match("\)",word)):
                tokens.append(f"Token (Agrupadores) : {word}")
                 
            elif(re.match("\[",word)):
                tokens.append(f"Token (Agrupadores) : {word}")
                 
            elif(re.match("\]",word)):
                tokens.append(f"Token (Agrupadores) : {word}")
                 
            elif(re.match(r"[>|<]",word)):
                tokens.append(f"Token (Operadores Relacionais) : {word}")
                
            if(re.match("==",word)):
                if(word.count("=") == 2):
                    tokens.append(f"Token (Atribuidor  Relacional) : {word}")

            elif(re.match("\{",word)):
                tokens.append(f"Token (Agrupadores) : {word}")
            
            elif(re.match("\}",word)):
                tokens.append(f"Token (Agrupadores) : {word}")

            elif(re.search(r"['\n' | '    ']+",word)):
                tokens.append(f"Token (Espaçador) : {word}")
            
            elif(re.search(r"[+|\-|*|/]+",word)):
                tokens.append(f"Token (Operadores Aritméticos) : {word}")
    
            source_index += 1
        
        return tokens

        re.purge();
