# Error handler; Raise MiniLangSyntaxError whenever a MiniLang error is encountered.
from src.shared.errors import MiniLangSyntaxError

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        
    def parse_program(self):
        # <program> -> [ <statement> ]*
        pass
        
    def parse_statement(self):
        # <statement> -> <declaration> | <assignment> | <print_statement>
        pass
        
    def parse_declaration(self):
        # <declaration> -> <type> identifier ";"
        pass
        
    def parse_assignment(self):
        # <assignment> -> identifier "=" <expression> ";"
        pass
        
    def parse_print_statement(self):
        # <print_statement> -> "print" "(" <expression> ")" ";"
        pass
        
    def parse_expression(self):
        # <expression> -> <term> { ( "+" | "-" ) <term> }
        pass
        
    def parse_term(self):
        # <term> -> <factor> { ( "*" | "/" ) <factor> }
        pass
        
    def parse_factor(self):
        # <factor> -> identifier | integer_literal | real_literal | "(" <expression> ")"
        pass