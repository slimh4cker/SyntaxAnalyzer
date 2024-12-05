# Generated from Hola.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,3,22,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,1,1,
        1,4,1,15,8,1,11,1,12,1,16,1,2,1,2,1,2,1,2,0,0,3,1,1,3,2,5,3,1,0,
        3,1,0,65,90,1,0,97,122,3,0,9,10,13,13,32,32,22,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,1,7,1,0,0,0,3,12,1,0,0,0,5,18,1,0,0,0,7,8,5,72,
        0,0,8,9,5,111,0,0,9,10,5,108,0,0,10,11,5,97,0,0,11,2,1,0,0,0,12,
        14,7,0,0,0,13,15,7,1,0,0,14,13,1,0,0,0,15,16,1,0,0,0,16,14,1,0,0,
        0,16,17,1,0,0,0,17,4,1,0,0,0,18,19,7,2,0,0,19,20,1,0,0,0,20,21,6,
        2,0,0,21,6,1,0,0,0,2,0,16,1,6,0,0
    ]

class HolaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    NAME = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Hola'" ]

    symbolicNames = [ "<INVALID>",
            "NAME", "WS" ]

    ruleNames = [ "T__0", "NAME", "WS" ]

    grammarFileName = "Hola.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


