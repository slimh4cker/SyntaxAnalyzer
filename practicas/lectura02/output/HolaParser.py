# Generated from Hola.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,3,6,2,0,7,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,4,0,2,1,0,0,0,2,3,5,
        1,0,0,3,4,5,2,0,0,4,1,1,0,0,0,0
    ]

class HolaParser ( Parser ):

    grammarFileName = "Hola.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Hola'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "NAME", "WS" ]

    RULE_saludar = 0

    ruleNames =  [ "saludar" ]

    EOF = Token.EOF
    T__0=1
    NAME=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SaludarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(HolaParser.NAME, 0)

        def getRuleIndex(self):
            return HolaParser.RULE_saludar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaludar" ):
                listener.enterSaludar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaludar" ):
                listener.exitSaludar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaludar" ):
                return visitor.visitSaludar(self)
            else:
                return visitor.visitChildren(self)




    def saludar(self):

        localctx = HolaParser.SaludarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_saludar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(HolaParser.T__0)
            self.state = 3
            self.match(HolaParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





