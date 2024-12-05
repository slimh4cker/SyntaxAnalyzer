from libs.src.controller.output.SlimParser import SlimParser
from libs.src.controller.output.SlimVisitor import SlimVisitor
from libs.src.utils.classes.ErrorVisitorHandler import ErrorVisitorHandler

class MyVisitor(SlimVisitor):
    def __init__(self):
        self.variables = {}
        self.output = []
        self.error_handler = ErrorVisitorHandler()

    def visitAssignment(self, ctx: SlimParser.AssignmentContext):
        variable_name = ctx.ID().getText()
        try:
            value = self.visit(ctx.expr())
            self.variables[variable_name] = value
        except NameError as e:
            self.output.append(str(e))

    def visitPrint(self, ctx: SlimParser.PrintContext):
        if ctx.ID():
            variable_name = ctx.ID().getText()
            if variable_name not in self.variables:
                line, column = ctx.start.line, ctx.start.column
                error_msg = self.error_handler.report_error(
                    line, column, f"Variable '{variable_name}' not initialized"
                )
                self.output.append(error_msg)
            else:
                value = self.variables[variable_name]
                print(value)
                self.output.append(value)
        elif ctx.expr():
            result = self.visit(ctx.expr())
            print(result)
            self.output.append(result)

    def visitSumRes(self, ctx: SlimParser.SumResContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left + right if ctx.SUM() else left - right

    def visitMulDiv(self, ctx: SlimParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.DIV() and right == 0:
            line = ctx.start.line
            column = ctx.start.column
            error_msg = f"at line {line}:{column}: Division by zero"
            self.output.append(error_msg)
        return left * right if ctx.POR() else left / right

    def visitExponential(self, ctx: SlimParser.ExponentialContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left ** right

    def visitVariableId(self, ctx: SlimParser.VariableIdContext):
        variable_name = ctx.ID().getText()
        return self.variables[variable_name]

    def visitNumber(self, ctx: SlimParser.NumberContext):
        return int(ctx.NUMBER().getText())

    def visitParenthesis(self, ctx: SlimParser.ParenthesisContext):
        return self.visit(ctx.expr())

