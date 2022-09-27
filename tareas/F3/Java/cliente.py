from antlr4 import *
from antlr.JavaParserListener import JavaParserListener
from antlr.JavaLexer import JavaLexer
from antlr.JavaParser import JavaParser
import sys

#PROBLEMA 1 IMPRIMIR TODAS LAS CLASES
class TreePrinter(JavaParserListener):
    def enterClassDeclaration(self, ctx: JavaParser.ClassDeclarationContext):
        print("---PROBLEMA 1---") #PRINT EXTRA PARA IDENTIFICAR DE QUE PROBLEMA SE ESTA IMPRIMIENDO
        print(ctx.identifier().getText())

#PROBLEMA 2 IMPRIMIR Los nombres de metodos y sus tipos

class TreePrinter2(JavaParserListener):
    def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        print("---PROBLEMA 2---")
        print(ctx.identifier().getText(),ctx.typeTypeOrVoid().getText())

#PROBLEMA 3 Imprimir todos los strings
class TreePrinter3(JavaParserListener):
    def enterStringLiteral(self, ctx: JavaParser.StringLiteralContext):
        print("---PROBLEMA 3---")
        print(ctx.STRING_LITERAL())


def main(argv):
    parser = JavaParser(CommonTokenStream(JavaLexer(FileStream("test.java"))))
    tree = parser.compilationUnit()
    print(tree)

    walker = ParseTreeWalker()
    walker.walk(TreePrinter(), tree)

    walker2 = ParseTreeWalker()  # Declaro otro walker para manejar otra clase de Tree printer para el otro problema de la tarea
    walker2.walk(TreePrinter2(), tree)

    walker3 = ParseTreeWalker() #Declaro un 3er walker
    walker3.walk(TreePrinter3(), tree)


if __name__ == '__main__':
    main("test.java")
