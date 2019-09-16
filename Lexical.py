import re

reservadas = [
    "int",
    "double",
    "if",
    "else",
    "while",
    "for",
    "do",
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
    "==",
    ">=",
    "<=",
]

caractere = [
    "!",
    "@",
    "$",
    "%",
    "¨¨",
    "&",
    "*",
    "§"
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

            if(word in reservadas):
                tokens.append([f"Token (Reservada) : {word}"])
            
            if(re.match("\W+",word) == None):
                if(re.match(r"[a-z|A-Z]+[0-9]+",word) and word not in reservadas):
                    tokens.append([f"Token (Identificador) : {word}"])
            
            if(word in caractere):
                tokens.append([f"Token não identificado : {word}"])

            elif(re.match("\d+\.\d+",word)):
                tokens.append([f"Token (Double) : {word}"])

            elif(re.match('\d+', word)):
                tokens.append([f"Token (Inteiro) : {word}"])

            elif(word in "=/*=-+"):
                tokens.append([f"Token (Atribuição) : {word}"])
            
            elif(re.match("\(",word)):
                tokens.append([f"Token (Agrupadores) : {word}"])
                 
            elif(re.match("\)",word)):
                tokens.append([f"Token (Agrupadores) : {word}"])
                 
            elif(re.match("\[",word)):
                tokens.append([f"Token (Agrupadores) : {word}"])
                 
            elif(re.match("\]",word)):
                tokens.append([f"Token (Agrupadores) : {word}"])
                 
            elif(re.match("\>",word)):
                tokens.append([f"Token (Comparador) : {word}"])
                
            elif(re.match("\<",word)):
                tokens.append([f"Token (Comparador) : {word}"])
                
            elif(re.match("\=+",word)):
                tokens.append([f"Token (Comparador) : {word}"])

            elif(re.match("\{",word)):
                tokens.append([f"Token (Agrupadores) : {word}"])
            
            elif(re.match("\}",word)):
                tokens.append([f"Token (Agrupadores) : {word}"])

            elif(re.match(r"(\n)+",word)):
                tokens.append([f"Token (Espaçador) : {word}"])
            
            elif("\#+" in word):
                tokens.append([f"Token (Comentário) : {word}"])       


            source_index += 1
        
        
        return tokens
