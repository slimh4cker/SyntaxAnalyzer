from antlr4 import *
from output.ExpresionLexer import ExpresionLexer
from output.ExpresionParser import ExpresionParser
from MyVisitor import MyVisitor


def main():
    input_stream = InputStream(input("Ingresa una expresion: "))
    lexer = ExpresionLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ExpresionParser(tokens)
    tree = parser.start()
    visitor = MyVisitor()
    result = visitor.visit(tree)
    print(result)


if __name__ == '__main__':
    main()
