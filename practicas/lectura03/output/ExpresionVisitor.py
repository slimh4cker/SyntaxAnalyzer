# Generated from Expresion.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpresionParser import ExpresionParser
else:
    from ExpresionParser import ExpresionParser

# This class defines a complete generic visitor for a parse tree produced by ExpresionParser.

class ExpresionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExpresionParser#start.
    def visitStart(self, ctx:ExpresionParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionParser#number.
    def visitNumber(self, ctx:ExpresionParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionParser#sumRes.
    def visitSumRes(self, ctx:ExpresionParser.SumResContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionParser#parenthesis.
    def visitParenthesis(self, ctx:ExpresionParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionParser#mulDiv.
    def visitMulDiv(self, ctx:ExpresionParser.MulDivContext):
        return self.visitChildren(ctx)



del ExpresionParser