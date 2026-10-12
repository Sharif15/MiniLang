from src.parser.ast_nodes import(
    Program,
    Declaration,
    Assignment,
    PrintStatement,
    Identifier,
    IntegerLiteral,
    RealLiteral,
    BinaryExpression
)

class DebugDisplay:
    def display_tokens(self, tokens):
        print("\n--- TOKENS ---")
        print(f"{'Line':<8} {'Type':<20} {'Value'}")

        for token in tokens:
            print(
                f"{token.line_number:<8} "
                f"{token.type:<20} "
                f"{token.value}"
            )


    def display_symbol_table(self, symbol_table):
        print("\n--- SYMBOL TABLE ---")
        symbol_table.display_table()


    def display_output(self, output):
        print("\n--- PROGRAM OUTPUT ---")

        for value in output:
            print(value)


    def display_ast(self, ast_root):
        # Prints AST
        print("\n--- AST ---")
        self._display_ast_node(ast_root, 0)


    # Helper function for display_ast
    def _display_ast_node(self, node, indent):
        prefix = "    " * indent

        if isinstance(node, Program):
            print(f"{prefix}Program")

            for statement in node.statements:
                self._display_ast_node(statement, indent + 1)

        elif isinstance(node, Declaration):
            print(
                f"{prefix}Declaration("
                f"type={node.var_type}, "
                f"name={node.name})"
            )

        elif isinstance(node, Assignment):
            print(f"{prefix}Assignment(name={node.name})")

            print(f"{prefix}    Expression:")
            self._display_ast_node(node.expression, indent + 2)

        elif isinstance(node, PrintStatement):
            print(f"{prefix}PrintStatement")

            print(f"{prefix}    Expression:")
            self._display_ast_node(node.expression, indent + 2)

        elif isinstance(node, Identifier):
            print(f"{prefix}Identifier(name={node.name})")

        elif isinstance(node, IntegerLiteral):
            print(f"{prefix}IntegerLiteral(value={node.value})")

        elif isinstance(node, RealLiteral):
            print(f"{prefix}RealLiteral(value={node.value})")

        elif isinstance(node, BinaryExpression):
            print(
                f"{prefix}BinaryExpression("
                f"operator={node.operator})"
            )

            print(f"{prefix}    Left:")
            self._display_ast_node(node.left, indent + 2)

            print(f"{prefix}    Right:")
            self._display_ast_node(node.right, indent + 2)

        else:
            print(f"{prefix}UnknownNode("f"{type(node).__name__})")


    def display_all(self, tokens, program, symbol_table, output):
        self.display_tokens(tokens)
        self.display_ast(program)
        self.display_symbol_table(symbol_table)
        self.display_output(output)