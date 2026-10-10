from src.shared.errors import MiniLangRuntimeError

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

class Interpreter:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

        # MiniLang print output gets stored here
        # This is for the debug mode
        self.output = []


    def execute(self, program_node):
        """
        Entry point for the interpreter.
        Executes the complete MiniLang program is source order.
        """
        for statement in program_node.statements:
            self.execute_statement(statement)


    def execute_statement(self, node):
        """
        Sends each statement node to its appropriate execution function.

        Raises a Python TypeError in case something goes
        wrong with OUR code, NOT the MiniLang program code.
        If raised, it's likely because the parser produced
        an supported node, which indicates a bug in our code.
        """
        if isinstance(node, Declaration):
            self.execute_declaration(node)

        elif isinstance(node, Assignment):
            self.execute_assignment(node)

        elif isinstance(node, PrintStatement):
            self.execute_print_statement(node)

        else:
            raise TypeError(
                node.line,
                f"Unsupported statement node: {type(node).__name__}"
            )


    def execute_declaration(self, node):
        """
        Handles a declaration during runtime.

        The declaration has already been placed into the symbol table
        during semantic analysis, so there is no new runtime action
        required here.

        We keep this function for the sake of uniformity and so the
        execute() function has somewhere to send Declaration nodes.
        """
        pass


    def execute_assignment(self, node):
        """
        Evaluates the RHS of an assignment and stores the 
        resulting runtime value in the symbol table.
        """
        value = self.evaluate_expression(node.expression)

        self.symbol_table.assign_value(
            node.name,
            value
        )


    def execute_print_statement(self, node):
        """
        Evaluates the expression supplied to print()
        and records its value as program output
        """
        value = self.evaluate_expression(node.expression)

        # Add to output array for debugging:
        self.output.append(value)

        # Normal program output:
        print(value)


    def evaluate_expression(self, node) -> int | float:
        """
        Evaluates any expression node and returns its runtime value.

        Raises MiniLangRuntimeError if type cannot be recognized.
        """
        if isinstance(node, IntegerLiteral):
            return node["value"]

        elif isinstance(node, RealLiteral):
            return node["value"]

        elif isinstance(node, Identifier):
            return self.evaluate_identifier(node)

        elif isinstance(node, BinaryExpression):
            return self.evaluate_binary_expression(node)

        else:
            raise MiniLangRuntimeError(
                node.line,
                f"Unknown expression type: {type(node).__name__}"
            )


    def evaluate_binary_expression(self, node) -> int | float:
        """
        Recursively evaluates a binary arithmetic expression.

        Raises MiniLangRuntimeError in the event of Division by zero.
        Raises MiniLangRuntimeError if operator cannot be recognized.
        """
        left_value = self.evaluate_expression(node.left)
        right_value = self.evaluate_expression(node.right)

        if node.operator == "+":
            return left_value + right_value

        elif node.operator == "-":
            return left_value - right_value

        elif node.operator == "*":
            return left_value * right_value

        elif node.operator == "/":
            if right_value == "0":
                raise MiniLangRuntimeError(
                    node.line,
                    "ZeroDivisionError"
                )

            return left_value / right_value 

        else:
            raise MiniLangRuntimeError(
                node.line,
                f"Unknown operator '{node.operator}'."
            )


    def evaluate_identifier(self, node) -> int | float:
        """
        Retrieves the current runtime value of a variable.
        """
        variable = self.symbol_table.get_variable(node.name)

        return variable["value"]
