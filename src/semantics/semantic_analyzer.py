class SemanticAnalyzer:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def analyze(self, program_node):
        # Entry point for semantic analysis; traverses the AST
        pass

    def analyze_statement(self, node):
        # Routes to declaration, assignment, or print analysis
        pass

    def analyze_declaration(self, node):
        # Checks symbol table if a variable is already declared. If yes, throws error.
        pass

    def analyze_assignment(self, node):
        # Checks if identifier is declared. Checks if <expression> type is compatible.
        pass

    def analyze_print_statement(self, node):
        # Verifies the <expression> is valid
        pass

    def analyze_expression(self, node):
        # Validates single expressions and returns type
        pass

    def analyze_binary_expression(self, node):
        # Validates terms and enforces Rule 4 (Arithmetic expression types)
        pass

    def analyze_identifier(self, node):
        # Checks if identifier is declared and initialized
        pass