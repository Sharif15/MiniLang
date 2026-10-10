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
        # Implement after agreement of AST node structure
        pass

    def display_all(self, tokens, program, symbol_table, output):
        self.display_tokens(tokens)
        self.display_ast(program)
        self.display_symbol_table(symbol_table)
        self.display_output(output)