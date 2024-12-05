# Generated from Slim.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SlimParser import SlimParser
else:
    from SlimParser import SlimParser

# This class defines a complete listener for a parse tree produced by SlimParser.
class SlimListener(ParseTreeListener):

    # Enter a parse tree produced by SlimParser#start.
    def enterStart(self, ctx:SlimParser.StartContext):
        pass

    # Exit a parse tree produced by SlimParser#start.
    def exitStart(self, ctx:SlimParser.StartContext):
        pass


    # Enter a parse tree produced by SlimParser#body.
    def enterBody(self, ctx:SlimParser.BodyContext):
        pass

    # Exit a parse tree produced by SlimParser#body.
    def exitBody(self, ctx:SlimParser.BodyContext):
        pass


    # Enter a parse tree produced by SlimParser#print.
    def enterPrint(self, ctx:SlimParser.PrintContext):
        pass

    # Exit a parse tree produced by SlimParser#print.
    def exitPrint(self, ctx:SlimParser.PrintContext):
        pass


    # Enter a parse tree produced by SlimParser#assignment.
    def enterAssignment(self, ctx:SlimParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SlimParser#assignment.
    def exitAssignment(self, ctx:SlimParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SlimParser#exponential.
    def enterExponential(self, ctx:SlimParser.ExponentialContext):
        pass

    # Exit a parse tree produced by SlimParser#exponential.
    def exitExponential(self, ctx:SlimParser.ExponentialContext):
        pass


    # Enter a parse tree produced by SlimParser#number.
    def enterNumber(self, ctx:SlimParser.NumberContext):
        pass

    # Exit a parse tree produced by SlimParser#number.
    def exitNumber(self, ctx:SlimParser.NumberContext):
        pass


    # Enter a parse tree produced by SlimParser#sumRes.
    def enterSumRes(self, ctx:SlimParser.SumResContext):
        pass

    # Exit a parse tree produced by SlimParser#sumRes.
    def exitSumRes(self, ctx:SlimParser.SumResContext):
        pass


    # Enter a parse tree produced by SlimParser#parenthesis.
    def enterParenthesis(self, ctx:SlimParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by SlimParser#parenthesis.
    def exitParenthesis(self, ctx:SlimParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by SlimParser#variableId.
    def enterVariableId(self, ctx:SlimParser.VariableIdContext):
        pass

    # Exit a parse tree produced by SlimParser#variableId.
    def exitVariableId(self, ctx:SlimParser.VariableIdContext):
        pass


    # Enter a parse tree produced by SlimParser#mulDiv.
    def enterMulDiv(self, ctx:SlimParser.MulDivContext):
        pass

    # Exit a parse tree produced by SlimParser#mulDiv.
    def exitMulDiv(self, ctx:SlimParser.MulDivContext):
        pass



del SlimParser