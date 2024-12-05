# Generated from Hola.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HolaParser import HolaParser
else:
    from HolaParser import HolaParser

# This class defines a complete listener for a parse tree produced by HolaParser.
class HolaListener(ParseTreeListener):

    # Enter a parse tree produced by HolaParser#saludar.
    def enterSaludar(self, ctx:HolaParser.SaludarContext):
        pass

    # Exit a parse tree produced by HolaParser#saludar.
    def exitSaludar(self, ctx:HolaParser.SaludarContext):
        pass



del HolaParser