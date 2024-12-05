from output.ExpresionVisitor import ExpresionVisitor


class MyVisitor(ExpresionVisitor):
    def visitExpresion(self, ctx):

        print("Se ingreso una expresion")