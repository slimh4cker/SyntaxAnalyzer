from output.HolaVisitor import HolaVisitor
from output.HolaParser import HolaParser


class MyVisitor(HolaVisitor):
    def visitSaludar(self, ctx):
        print("Se ingreso un saludo")
