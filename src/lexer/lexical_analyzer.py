# Error handler; Raise LexicalError whenever a MiniLang error is encountered.
from src.shared.errors import LexicalError

class Token:
    def __init__(self, type, value, line_number):
        self.type = type
        self.value = value
        self.line_number = line_number
        
    def __repr__(self): 
        return (
            f"Token(type={self.type!r}, {self.value!r}, " 
            f"line ={self.line_number})" 
        )

class LexicalAnalyzer:
    
    KEYWORDS = { 
                
        "int": "INT", 
        "real": "REAL", 
        "print": "PRINT",
    }    
    
    SINGLE_CHAR_TOKENS = { 
                          
        "=": "ASSIGN",
        "+": "PLUS", 
        "-": "MINUS",
        "*": "MULTIPLY",
        "/": "DIVIDE",
        "(": "LEFT_PAREN",
        ")": "RIGHT_PAREN",
        ";": "SEMICOLON",
    }
    
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.current_line = 1
    
    # looking at next without advancing 
    
    def _peak(self):
        if self.position >= len(self.source_code):
            return None
        
        return self.source_code[self.position]
    
    def _advance(self):
        char = self._peak()
        
        if char is not None:
            self.position += 1
            
            if char == "\n":
                self.current_line += 1
        
        return char
    
    def get_next_token(self):
        # Parses the next valid character(s) and returns a Token object
        
        while (self._peak() is not None and self._peak().isspace()):
            self._advance()
        
        char = self._peak()
        
        if char is None: 
            return None
        
        line = self.current_line
        
        # Identifiers and keywords 
        if char.isalpha() or char == "_": 
            start = self.position 
            
            while self._peak() is not None and ( self._peak().isalnum() or self._peak() == "_" ): 
                self._advance() 
                
            value = self.source_code[start:self.position] 
            token_type = self.KEYWORDS.get(value, "IDENTIFIER") 
            return Token(token_type, value, line)
        
        # Numeric literals 
        if char.isdigit():
            start = self.position
            while ( self._peak() is not None and self._peak().isdigit() ):
                self._advance() 
                
            token_type = "INTEGER_LITERAL" 
            if self._peak() == ".": 
                self._advance() 
            
                if self._peak() is None or not self._peak().isdigit() :
                    
                    invalid_value = self.source_code[ start:self.position ]
                    raise LexicalError(line, f"Invalid real literal '{invalid_value}'.") 
                
                while ( self._peak() is not None and self._peak().isdigit() ): 
                    self._advance() 
                    
                token_type = "REAL_LITERAL" 
                
            value = self.source_code[start:self.position] 
            return Token(token_type, value, line)
        
        # Operators and punctuation
        if char in self.SINGLE_CHAR_TOKENS:
            self._advance() 
            
            return Token( self.SINGLE_CHAR_TOKENS[char], char, line, )
        
        # Invalid character
        
        self._advance() 
        
        raise LexicalError(line, f"Invalid character '{char}'.")
        
    def tokenize(self):
        # Loops through the source code and returns a list of all tokens
        # Must recognize INT, REAL, PRINT, IDENTIFIER, INTEGER_LITERAL, REAL_LITERAL, 
        # ASSIGN, PLUS, MINUS, MULTIPLY, DIVIDE, LEFT_PAREN, RIGHT_PAREN, SEMICOLON
        
        tokens = []
        
        while True:
            token = self.get_next_token()
            
            if token is None:
                break
            
            tokens.append(token)
            
        return tokens
            
        
        pass