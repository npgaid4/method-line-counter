from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from src.ast.Java8Lexer import Java8Lexer
from src.ast.Java8Parser import Java8Parser
from pprint import pformat


class AstProcessor:

    def __init__(self, listener):
        self.listener = listener

    def execute(self, input_source):
        parser = Java8Parser(CommonTokenStream(Java8Lexer(FileStream(input_source, encoding="utf-8"))))
        walker = ParseTreeWalker()
        walker.walk(self.listener, parser.compilationUnit())
        return self.listener.ast_info