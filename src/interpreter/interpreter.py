class Interpreter:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def execute(self, program_node):
        # Processes program statements in source order
        pass

    def execute_statement(self, node):
        # Routes to appropriate statement execution function
        pass

    def execute_declaration(self, node):
        # May be a pass if semantic analyzer populated the symbol table
        pass

    def execute_assignment(self, node):
        # Evaluates expression and stores result in symbol table
        pass

    def execute_print_statement(self, node):
        # Evaluates statement and prints result to console
        pass

    def evaluate_expression(self, node):
        # Returns the numeric value of a given node
        pass

    def evaluate_binary_expression(self, node):
        # Evaluates arithmetic, handles division by zero, and returns calculated value
        pass

    def evaluate_identifier(self, node):
        # Returns the current runtime value of an identifier
        pass