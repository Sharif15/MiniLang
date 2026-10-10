# Error handler; Raise LexicalError whenever a MiniLang error is encountered.
from src.shared.errors import LexicalError

class Token:
    def __init__(self, type, value, line_number):
        self.type = type
        self.value = value
        self.line_number = line_number

class LexicalAnalyzer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.current_line = 1
        
    def get_next_token(self):
        # Parses the next valid character(s) and returns a Token object
        pass
        
    def tokenize(self):
        # Loops through the source code and returns a list of all tokens
        # Must recognize INT, REAL, PRINT, IDENTIFIER, INTEGER_LITERAL, REAL_LITERAL, 
        # ASSIGN, PLUS, MINUS, MULTIPLY, DIVIDE, LEFT_PAREN, RIGHT_PAREN, SEMICOLON
        pass