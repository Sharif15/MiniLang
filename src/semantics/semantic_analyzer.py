from src.shared.errors import SemanticError

# Must import AST node classes; Please update if the ast_nodes are stored elsewhere!
# Also update if the names for your classes are different from what they are here!
from src.parser.parser import (
    Declaration,
    Assignment,
    PrintStatement,
    Identifier,
    IntegerLiteral,
    RealLiteral,
    BinaryExpression
)

class SemanticAnalyzer:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table


    def analyze(self, program_node):
        """
        Entry point for static semantic analysis. Performs semantic
        analysis on a MiniLang AST produced by the parser.

        Processes statements in source order so declaration-before-use
        and initialization-before-use rules can be enforced correctly.
        """
        for statement in program_node.statements:
            self.analyze_statement(statement)


    def analyze_statement(self, node):
        """
        Sends each statement node to its appropriate analysis function

        Raises a Python TypeError in case something goes
        wrong with OUR code, NOT the MiniLang program code.
        If raised, it's likely because the parser produced
        an supported node, which indicates a bug in our code.
        """
        if isinstance(node, Declaration):
            self.analyze_declaration(node)

        elif isinstance(node, Assignment):
            self.analyze_assignment(node)

        elif isinstance(node, PrintStatement):
            self.analyze_print_statement(node)

        else:
            raise TypeError(
                node.line,
                f"Unsupported statement node: {type(node).__name__}"
            )


    def analyze_declaration(self, node):
        """
        Analyzes a variable declaration statement.

        Checks that the variable has not already been declared,
        then adds it to the symbol table. 

        Raises SemanticError if it has been declared already.
        """
        variable = self.symbol_table.get_variable(node.name)

        if variable is not None:
            raise SemanticError(
                node.line,
                f"Variable '{node.name}' is already declared."
            )

        self.symbol_table.declare_variable(
            node.name,
            node.var_type
        )


    def analyze_assignment(self, node):
        """
        Analyzes an assignment statement.

        Checks if an assignment target is declared.
        Checks if the RHS expression is semantically valid.
        Checks if the RHS type is compatible with target type.

        If successful, marks the variable as semantically initialized.
        
        Raises SemanticError if variable is not declared.
        Raises SemanticError if types are incompatible
        """
        variable = self.symbol_table.get_variable(node.name)

        if variable is None:
            raise SemanticError(
                node.line,
                f"Variable '{node.name}' is not declared."
            )

        # Analyze RHS and confirm type compatibility:
        # real -> int is NOT allowed
        expression_type = self.analyze_expression(
            node.expression
        )

        if variable["type"] == "int" and expression_type == "real":
            raise SemanticError(
                node.line,
                f"Cannot assign real value to int variable '{node.name}'."
            )

        # Semantic initialization only, value is assigned during interpretation
        self.symbol_table.mark_initialized(node.name)


    def analyze_print_statement(self, node):
        """
        Ensures the expression supplied to print() is semantically valid.
        """
        self.analyze_expression(node.expression)


    def analyze_expression(self, node) -> str:
        """
        Analyzes any expression and returns its MiniLang type (int or real) as a string.
        
        Raises SemanticError if type cannot be recognzied.
        """
        if isinstance(node, IntegerLiteral):
            return "int"

        elif isinstance(node, RealLiteral):
            return "real"

        elif isinstance(node, Identifier):
            return self.analyze_identifier(node)

        elif isinstance(node, BinaryExpression):
            return self.analyze_binary_expression(node)

        else:
            raise SemanticError(
                node.line,
                f"Unknown expression type: {type(node).__name__}"
            )


    def analyze_binary_expression(self, node) -> str:
        """
        Analyzes an arithmetic binary expression.

        Enforces the following MiniLang rules:
            int op int -> int
            int op real -> real
            real op int -> real
            real op real -> real
        """
        left_type = self.analyze_expression(node.left)
        right_type = self.analyze_expression(node.right)

        if left_type == "real" or right_type == "real":
            return "real"

        return "int"


    def analyze_identifier(self, node) -> str:
        """
        Handles an identifier whose current value is being read.

        Checks if a variable has been declared.
        Checks if a variable has been initialized.

        Returns its declared type as a string.

        Raises SemanticError if variable has not been declared.
        Raises SemanticError if variable has not been initialized.
        """
        variable = self.symbol_table.get_variable(node.name)

        if variable is None:
            raise SemanticError(
                node.line,
                f"Variable '{node.name}' is not declared."
            )

        if not variable["initialized"]:
            raise SemanticError(
                node.line,
                f"Variable '{node.name}' is not initialized."
            )

        return variable["type"]
