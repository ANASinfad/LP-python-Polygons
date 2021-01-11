from antlr4 import *

from cl.ConvexPolygonLexer import ConvexPolygonLexer
from cl.ConvexPolygonParser import ConvexPolygonParser


def execute_script(entry, visitor):
    input_stream = InputStream(entry)
    if str(input_stream) != "exit":
        lexer = ConvexPolygonLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ConvexPolygonParser(token_stream)
        tree = parser.root()
        return visitor.visit(tree)
