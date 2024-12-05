# Generated from Hola.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HolaParser import HolaParser
else:
    from HolaParser import HolaParser

# This class defines a complete generic visitor for a parse tree produced by HolaParser.

class HolaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HolaParser#saludar.
    def visitSaludar(self, ctx:HolaParser.SaludarContext):
        return self.visitChildren(ctx)



del HolaParser