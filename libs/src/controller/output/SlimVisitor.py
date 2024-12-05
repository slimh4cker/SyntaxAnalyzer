# Generated from Slim.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SlimParser import SlimParser
else:
    from SlimParser import SlimParser

# This class defines a complete generic visitor for a parse tree produced by SlimParser.

class SlimVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SlimParser#start.
    def visitStart(self, ctx:SlimParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlimParser#body.
    def visitBody(self, ctx:SlimParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlimParser#print.
    def visitPrint(self, ctx:SlimParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlimParser#assignment.
    def visitAssignment(self, ctx:SlimParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlimParser#exponential.
    def visitExponential(self, ctx:SlimParser.ExponentialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlimParser#number.
    def visitNumber(self, ctx:SlimParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlimParser#sumRes.
    def visitSumRes(self, ctx:SlimParser.SumResContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlimParser#parenthesis.
    def visitParenthesis(self, ctx:SlimParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlimParser#variableId.
    def visitVariableId(self, ctx:SlimParser.VariableIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlimParser#mulDiv.
    def visitMulDiv(self, ctx:SlimParser.MulDivContext):
        return self.visitChildren(ctx)



del SlimParser