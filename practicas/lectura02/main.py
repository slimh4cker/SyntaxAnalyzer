from antlr4 import *
from output.HolaLexer import HolaLexer
from output.HolaParser import HolaParser
from MyVisitor import MyVisitor


def main():
    input_stream = InputStream(input("Ingresa data:"))
    # Crear lexico
    lexer = HolaLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    # Creamos el sintactico
    parse = HolaParser(tokens)
    # llamar a la main rule
    # Crear arbol sintactico
    tree = parse.saludar()

    visitor = MyVisitor()
    result = visitor.visit(tree)
    print(result)


if __name__ == '__main__':
    main()
