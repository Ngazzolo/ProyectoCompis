from util.exceptions import *
from antlr.coolListener import coolListener
from antlr.coolParser import coolParser


class SemanticListener(coolListener):
    def __init__(self):
        self.main = False

#Problema 1 lista profe
    def exitAttribute(self, ctx:coolParser.AttributeContext):
        if ctx.ID().getText() == 'self':
            raise BadAttributeName();
        #print(ctx.ID().getText())

# Enter a parse tree produced by coolParser#let_decl.

#Problema 6 Nicolas Ver definiciòn de variable let y validar que el id no tenga string self
    def exitLet_decl(self, ctx:coolParser.Let_declContext):
        if ctx.ID().getText() == 'self' :
            raise BadVariableName();