# Error handler; Raise MiniLangSyntaxError whenever a MiniLang error is encountered.
from src.shared.errors import MiniLangSyntaxError

from src.parser.ast_nodes import (
    Program,
    Declaration,
    Assignment,
    PrintStatement,
    Identifier,
    IntegerLiteral,
    RealLiteral,
    BinaryExpression
)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        
        if tokens:
            self.current_token = tokens[0]
        else:
            self.current_token = None
    
    # Helper functions 
    
    def _advance(self):
        # Move to the next token
        
        self.position += 1

        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None

    def _error(self, message):
        # Raise a syntax error with its line number
        
        if self.current_token is not None:
            line = self.current_token.line_number
            value = self.current_token.value

            raise MiniLangSyntaxError(
                line,
                f"{message} Found '{value}'."
            )

        line = self.tokens[-1].line_number if self.tokens else 1

        raise MiniLangSyntaxError(
            line,
            f"{message} Found end of input."
        )

    def _eat(self, expected_type):
        # Consume a token if it matches the expected type
        
        if (
            self.current_token is not None
            and self.current_token.type == expected_type
        ):
            token = self.current_token
            self._advance()
            return token

        self._error(f"Expected {expected_type}.")

    
    def parse_program(self):
        # <program> -> [ <statement> ]*
        
        statements = []

        while self.current_token is not None:
            statements.append(self.parse_statement())

        return Program(statements=statements)
        
    def parse_statement(self):
        # <statement> -> <declaration> | <assignment> | <print_statement>
        
        if self.current_token is None:
            self._error("Expected a statement.")

        token_type = self.current_token.type

        if token_type in ("INT", "REAL"):
            return self.parse_declaration()

        if token_type == "IDENTIFIER":
            return self.parse_assignment()

        if token_type == "PRINT":
            return self.parse_print_statement()

        self._error(
            "Expected a declaration, assignment, or print statement."
        )
        
        
    def parse_declaration(self):
        # <declaration> -> <type> identifier ";"
        
        type_token = self.current_token

        if type_token.type == "INT":
            self._eat("INT")
            var_type = "int"
        elif type_token.type == "REAL":
            self._eat("REAL")
            var_type = "real"
        else:
            self._error("Expected type 'int' or 'real'.")

        name_token = self._eat("IDENTIFIER")
        self._eat("SEMICOLON")

        return Declaration(
            var_type=var_type,
            name=name_token.value,
            line=type_token.line_number,
        )
        
    def parse_assignment(self):
        # <assignment> -> identifier "=" <expression> ";"
        
        name_token = self._eat("IDENTIFIER")
        self._eat("ASSIGN")

        expression = self.parse_expression()

        self._eat("SEMICOLON")

        return Assignment(
            name=name_token.value,
            expression=expression,
            line=name_token.line_number,
        )
        
    def parse_print_statement(self):
        # <print_statement> -> "print" "(" <expression> ")" ";"
        
        print_token = self._eat("PRINT")
        self._eat("LEFT_PAREN")

        expression = self.parse_expression()

        self._eat("RIGHT_PAREN")
        self._eat("SEMICOLON")

        return PrintStatement(
            expression=expression,
            line=print_token.line_number,
        )
        
    def parse_expression(self):
        # <expression> -> <term> { ( "+" | "-" ) <term> }
        
        node = self.parse_term()

        while (
            self.current_token is not None
            and self.current_token.type in ("PLUS", "MINUS")
        ):
            operator_token = self.current_token
            self._advance()

            right = self.parse_term()

            node = BinaryExpression(
                left=node,
                operator=operator_token.value,
                right=right,
                line=operator_token.line_number,
            )

        return node
        
    def parse_term(self):
        # <term> -> <factor> { ( "*" | "/" ) <factor> }
        
        node = self.parse_factor()

        while (
            self.current_token is not None
            and self.current_token.type in ("MULTIPLY", "DIVIDE")
        ):
            operator_token = self.current_token
            self._advance()

            right = self.parse_factor()

            node = BinaryExpression(
                left=node,
                operator=operator_token.value,
                right=right,
                line=operator_token.line_number,
            )

        return node
        
    def parse_factor(self):
        # <factor> -> identifier | integer_literal | real_literal | "(" <expression> ")"
    
        if self.current_token is None:
            self._error("Expected an expression.")

        token = self.current_token

        if token.type == "IDENTIFIER":
            self._advance()

            return Identifier(
                name=token.value,
                line=token.line_number,
            )

        if token.type == "INTEGER_LITERAL":
            self._advance()

            return IntegerLiteral(
                value=int(token.value),
                line=token.line_number,
            )

        if token.type == "REAL_LITERAL":
            self._advance()

            return RealLiteral(
                value=float(token.value),
                line=token.line_number,
            )

        if token.type == "LEFT_PAREN":
            self._advance()

            node = self.parse_expression()

            self._eat("RIGHT_PAREN")

            return node

        self._error(
            "Expected an identifier, numeric literal, "
            "or parenthesized expression."
        )
