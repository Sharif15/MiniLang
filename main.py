import sys
import argparse
from src.lexer.lexical_analyzer import LexicalAnalyzer
from src.parser.parser import Parser
from src.shared.symbol_table import SymbolTable
from src.semantics.semantic_analyzer import SemanticAnalyzer
from src.interpreter.interpreter import Interpreter

def main():
    # Set up argument parsing for the source file and debug flag
    arg_parser = argparse.ArgumentParser(description="MiniLang Interpreter")
    arg_parser.add_argument("source_file", help="Path to the MiniLang source file (.mini)")
    arg_parser.add_argument("--debug", action="store_true", help="Enable debug/display mode")
    args = arg_parser.parse_args()

    try:
        # 1. Read source code
        with open(args.source_file, 'r') as file:
            source_code = file.read()

        # 2. Lexical Analysis
        lexer = LexicalAnalyzer(source_code)
        tokens = lexer.tokenize()
        if args.debug:
            print("--- TOKENS ---")
            for token in tokens:
                print(f"{token.type}: {token.value}")

        # 3. Syntax Analysis (Parsing)
        parser = Parser(tokens)
        ast_root = parser.parse_program()
        if args.debug:
            print("\n--- AST ---")
            # Call your AST print/display function here

        # 4. Shared Symbol Table
        symbol_table = SymbolTable()

        # 5. Semantic Analysis
        semantic_analyzer = SemanticAnalyzer(symbol_table)
        semantic_analyzer.analyze(ast_root)

        # 6. Interpretation / Execution
        if args.debug:
            print("\n--- PROGRAM OUTPUT ---")
            
        interpreter = Interpreter(symbol_table)
        interpreter.execute(ast_root)

        if args.debug:
            print("\n--- SYMBOL TABLE ---")
            symbol_table.display_table()

    except FileNotFoundError:
        print(f"Error: Could not find file '{args.source_file}'")
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()