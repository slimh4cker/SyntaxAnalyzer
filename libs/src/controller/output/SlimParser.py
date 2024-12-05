# Generated from Slim.g4 by ANTLR 4.13.2
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
        4,1,17,60,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,2,1,2,3,
        2,28,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        3,4,44,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,55,8,4,10,4,12,
        4,58,9,4,1,4,0,1,8,5,0,2,4,6,8,0,2,1,0,8,9,1,0,10,11,63,0,10,1,0,
        0,0,2,22,1,0,0,0,4,27,1,0,0,0,6,31,1,0,0,0,8,43,1,0,0,0,10,11,5,
        1,0,0,11,12,5,2,0,0,12,13,3,2,1,0,13,14,5,3,0,0,14,1,1,0,0,0,15,
        21,3,4,2,0,16,21,3,6,3,0,17,18,3,8,4,0,18,19,5,4,0,0,19,21,1,0,0,
        0,20,15,1,0,0,0,20,16,1,0,0,0,20,17,1,0,0,0,21,24,1,0,0,0,22,20,
        1,0,0,0,22,23,1,0,0,0,23,3,1,0,0,0,24,22,1,0,0,0,25,28,5,14,0,0,
        26,28,3,8,4,0,27,25,1,0,0,0,27,26,1,0,0,0,28,29,1,0,0,0,29,30,5,
        4,0,0,30,5,1,0,0,0,31,32,5,14,0,0,32,33,5,5,0,0,33,34,3,8,4,0,34,
        35,5,4,0,0,35,7,1,0,0,0,36,37,6,4,-1,0,37,38,5,6,0,0,38,39,3,8,4,
        0,39,40,5,7,0,0,40,44,1,0,0,0,41,44,5,13,0,0,42,44,5,14,0,0,43,36,
        1,0,0,0,43,41,1,0,0,0,43,42,1,0,0,0,44,56,1,0,0,0,45,46,10,6,0,0,
        46,47,7,0,0,0,47,55,3,8,4,7,48,49,10,5,0,0,49,50,7,1,0,0,50,55,3,
        8,4,6,51,52,10,4,0,0,52,53,5,12,0,0,53,55,3,8,4,5,54,45,1,0,0,0,
        54,48,1,0,0,0,54,51,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,
        0,0,0,57,9,1,0,0,0,58,56,1,0,0,0,6,20,22,27,43,54,56
    ]

class SlimParser ( Parser ):

    grammarFileName = "Slim.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Slim^'", "'{'", "'}'", "';'", "'='", 
                     "'('", "')'", "'*'", "'/'", "'+'", "'-'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "POR", "DIV", "SUM", "RES", "EXP", "NUMBER", "ID", 
                      "LINE_COMMENT", "BLOCK_COMMENT", "WS" ]

    RULE_start = 0
    RULE_body = 1
    RULE_print = 2
    RULE_assignment = 3
    RULE_expr = 4

    ruleNames =  [ "start", "body", "print", "assignment", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    POR=8
    DIV=9
    SUM=10
    RES=11
    EXP=12
    NUMBER=13
    ID=14
    LINE_COMMENT=15
    BLOCK_COMMENT=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.errors = []
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(SlimParser.BodyContext,0)


        def getRuleIndex(self):
            return SlimParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = SlimParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(SlimParser.T__0)
            self.state = 11
            self.match(SlimParser.T__1)
            self.state = 12
            self.body()
            self.state = 13
            self.match(SlimParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    def notifyErrorListeners(self, msg, offendingToken, e):
        line = offendingToken.line
        column = offendingToken.column
        message = f"Syntax Error: at line: {line}:{column} - {msg}"
        self.errors.append(message)
        super().notifyErrorListeners(msg, offendingToken, e)
        
    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlimParser.PrintContext)
            else:
                return self.getTypedRuleContext(SlimParser.PrintContext,i)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlimParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(SlimParser.AssignmentContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlimParser.ExprContext)
            else:
                return self.getTypedRuleContext(SlimParser.ExprContext,i)


        def getRuleIndex(self):
            return SlimParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = SlimParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 24640) != 0):
                self.state = 20
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 15
                    self.print_()
                    pass

                elif la_ == 2:
                    self.state = 16
                    self.assignment()
                    pass

                elif la_ == 3:
                    self.state = 17
                    self.expr(0)
                    self.state = 18
                    self.match(SlimParser.T__3)
                    pass


                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SlimParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(SlimParser.ExprContext,0)


        def getRuleIndex(self):
            return SlimParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = SlimParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 25
                self.match(SlimParser.ID)
                pass

            elif la_ == 2:
                self.state = 26
                self.expr(0)
                pass


            self.state = 29
            self.match(SlimParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SlimParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(SlimParser.ExprContext,0)


        def getRuleIndex(self):
            return SlimParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = SlimParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(SlimParser.ID)
            self.state = 32
            self.match(SlimParser.T__4)
            self.state = 33
            self.expr(0)
            self.state = 34
            self.match(SlimParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SlimParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExponentialContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SlimParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlimParser.ExprContext)
            else:
                return self.getTypedRuleContext(SlimParser.ExprContext,i)

        def EXP(self):
            return self.getToken(SlimParser.EXP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponential" ):
                listener.enterExponential(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponential" ):
                listener.exitExponential(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponential" ):
                return visitor.visitExponential(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SlimParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(SlimParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class SumResContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SlimParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlimParser.ExprContext)
            else:
                return self.getTypedRuleContext(SlimParser.ExprContext,i)

        def SUM(self):
            return self.getToken(SlimParser.SUM, 0)
        def RES(self):
            return self.getToken(SlimParser.RES, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumRes" ):
                listener.enterSumRes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumRes" ):
                listener.exitSumRes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumRes" ):
                return visitor.visitSumRes(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SlimParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SlimParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesis" ):
                listener.enterParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesis" ):
                listener.exitParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class VariableIdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SlimParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SlimParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableId" ):
                listener.enterVariableId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableId" ):
                listener.exitVariableId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableId" ):
                return visitor.visitVariableId(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SlimParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlimParser.ExprContext)
            else:
                return self.getTypedRuleContext(SlimParser.ExprContext,i)

        def POR(self):
            return self.getToken(SlimParser.POR, 0)
        def DIV(self):
            return self.getToken(SlimParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SlimParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = SlimParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 37
                self.match(SlimParser.T__5)
                self.state = 38
                self.expr(0)
                self.state = 39
                self.match(SlimParser.T__6)
                pass
            elif token in [13]:
                localctx = SlimParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.match(SlimParser.NUMBER)
                pass
            elif token in [14]:
                localctx = SlimParser.VariableIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(SlimParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 54
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = SlimParser.MulDivContext(self, SlimParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 46
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 47
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = SlimParser.SumResContext(self, SlimParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 49
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 50
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = SlimParser.ExponentialContext(self, SlimParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 52
                        self.match(SlimParser.EXP)
                        self.state = 53
                        self.expr(5)
                        pass

             
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




