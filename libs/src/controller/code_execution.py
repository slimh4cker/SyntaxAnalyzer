from antlr4 import InputStream, CommonTokenStream
from libs.src.controller.MyVisitor import MyVisitor
from libs.src.controller.output.SlimLexer import SlimLexer
from libs.src.controller.output.SlimParser import SlimParser


def execute_code(input_code):
    try:
        input_stream = InputStream(input_code)
        lexer = SlimLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = SlimParser(tokens)
        tree = parser.start()
        errors = lexer.errors + parser.errors
        if errors:
            return "\n".join(errors)
        visitor = MyVisitor()
        visitor.visit(tree)
        result = "\n".join(map(str, visitor.output))
        return result
    except Exception as e:
        return f"Error: {str(e)}"



