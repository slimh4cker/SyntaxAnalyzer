from output.ExpresionVisitor import ExpresionVisitor
from output.ExpresionParser import ExpresionParser


class MyVisitor(ExpresionVisitor):
    def visitSumRes(self, ctx: ExpresionParser.SumResContext):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        return left + right if ctx.SUM() else left - right if ctx.RES() else None

    def visitMulDiv(self, ctx: ExpresionParser.MulDivContext):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        return left * right if ctx.POR() else left / right if ctx.DIV() else None

    def visitNumber(self, ctx):
        return ctx.NUMBER().getText()

    def visitParenthesis(self, ctx: ExpresionParser.ParenthesisContext):
        return self.visit(ctx.expr())
