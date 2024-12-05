# Generated from Expresion.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpresionParser import ExpresionParser
else:
    from ExpresionParser import ExpresionParser

# This class defines a complete listener for a parse tree produced by ExpresionParser.
class ExpresionListener(ParseTreeListener):

    # Enter a parse tree produced by ExpresionParser#start.
    def enterStart(self, ctx:ExpresionParser.StartContext):
        pass

    # Exit a parse tree produced by ExpresionParser#start.
    def exitStart(self, ctx:ExpresionParser.StartContext):
        pass


    # Enter a parse tree produced by ExpresionParser#number.
    def enterNumber(self, ctx:ExpresionParser.NumberContext):
        pass

    # Exit a parse tree produced by ExpresionParser#number.
    def exitNumber(self, ctx:ExpresionParser.NumberContext):
        pass


    # Enter a parse tree produced by ExpresionParser#sumRes.
    def enterSumRes(self, ctx:ExpresionParser.SumResContext):
        pass

    # Exit a parse tree produced by ExpresionParser#sumRes.
    def exitSumRes(self, ctx:ExpresionParser.SumResContext):
        pass


    # Enter a parse tree produced by ExpresionParser#parenthesis.
    def enterParenthesis(self, ctx:ExpresionParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by ExpresionParser#parenthesis.
    def exitParenthesis(self, ctx:ExpresionParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by ExpresionParser#mulDiv.
    def enterMulDiv(self, ctx:ExpresionParser.MulDivContext):
        pass

    # Exit a parse tree produced by ExpresionParser#mulDiv.
    def exitMulDiv(self, ctx:ExpresionParser.MulDivContext):
        pass



del ExpresionParser