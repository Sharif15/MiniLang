import sys
import argparse

from src.lexer.lexical_analyzer import LexicalAnalyzer
from src.parser.parser import Parser
from src.shared.symbol_table import SymbolTable
from src.shared.errors import MiniLangError
from src.shared.debug import DebugDisplay
from src.semantics.semantic_analyzer import SemanticAnalyzer
from src.interpreter.interpreter import Interpreter

def main():
    # Set up argument parsing for the source file and debug flag
    arg_parser = argparse.ArgumentParser(description="MiniLang Interpreter")
    arg_parser.add_argument("source_file", help="Path to the MiniLang source file (.mini)")
    arg_parser.add_argument("--debug", action="store_true", help="Enable debug/display mode")
    args = arg_parser.parse_args()

    debug_display = DebugDisplay()

    try:
        # 1. Read source code
        with open(args.source_file, 'r') as file:
            source_code = file.read()

        # 2. Lexical Analysis
        lexer = LexicalAnalyzer(source_code)
        tokens = lexer.tokenize()
        
            # Debug/Display Mode; Tokens:
        if args.debug:
            debug_display.display_tokens(tokens)

        # 3. Syntax Analysis (Parsing)
        parser = Parser(tokens)
        ast_root = parser.parse_program()

            # Debug/Display Mode; AST:
        if args.debug:
            debug_display.display_ast(ast_root)

        # 4. Shared Symbol Table
        symbol_table = SymbolTable()

        # 5. Semantic Analysis
        semantic_analyzer = SemanticAnalyzer(symbol_table)
        semantic_analyzer.analyze(ast_root)

            # Symantic analysis uses initialized flags to determine whether
            # reads were legal. We reset those flags before actual execution
            # so that the interpreter can establish true runtime state.
        symbol_table.reset_runtime_state() 

        # 6. Interpretation / Execution 
        interpreter = Interpreter(symbol_table)
        interpreter.execute(ast_root)

            # Debug/Display Mode; Program Output & Symbol Table:
        if args.debug:
            debug_display.display_symbol_table(symbol_table)
            debug_display.display_output(interpreter.output)
        else: # Print normal program execution output for non-debug mode:
            for value in interpreter.output:
                print(value)


    except FileNotFoundError:
        print(f"Error: Could not find file '{args.source_file}'")
        sys.exit(1)

    # MiniLang Error Handler:
    except MiniLangError as error:
        print(error)
        sys.exit(1)
        
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()