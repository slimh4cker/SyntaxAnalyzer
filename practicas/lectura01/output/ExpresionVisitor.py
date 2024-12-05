# Generated from Expresion.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpresionParser import ExpresionParser
else:
    from ExpresionParser import ExpresionParser

# This class defines a complete generic visitor for a parse tree produced by ExpresionParser.

class ExpresionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExpresionParser#expresion.
    def visitExpresion(self, ctx:ExpresionParser.ExpresionContext):
        return self.visitChildren(ctx)



del ExpresionParser