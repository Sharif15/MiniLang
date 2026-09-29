import unittest
import io
import sys

from src.lexer.lexical_analyzer import LexicalAnalyzer
from src.parser.parser import Parser
from src.shared.symbol_table import SymbolTable
from src.semantics.semantic_analyzer import SemanticAnalyzer
from src.interpreter.interpreter import Interpreter

class TestMiniLangInterpreter(unittest.TestCase):
    
    def run_interpreter(self, source_code):
        """Helper method to run source code through the entire pipeline and capture output."""
        captured_output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output
        
        try:
            lexer = LexicalAnalyzer(source_code)
            tokens = lexer.tokenize()
            
            parser = Parser(tokens)
            ast_root = parser.parse_program()
            
            symbol_table = SymbolTable()
            
            semantic_analyzer = SemanticAnalyzer(symbol_table)
            semantic_analyzer.analyze(ast_root)
            
            interpreter = Interpreter(symbol_table)
            interpreter.execute(ast_root)
            
            sys.stdout = original_stdout
            return captured_output.getvalue().strip(), None
            
        except Exception as e:
            sys.stdout = original_stdout
            return None, str(e)

    def test_01_basic_declaration_and_assignment(self):
        # Covers: Basic variable declaration and assignment, int variables
        source = "int x; x = 10; print(x);"
        output, error = self.run_interpreter(source)
        self.assertEqual(output, "10")
        self.assertIsNone(error)

    def test_02_arithmetic_and_precedence(self):
        # Covers: Arithmetic expressions, Operator precedence
        source = "int x; x = 5 + 10 * 2; print(x);"
        output, error = self.run_interpreter(source)
        self.assertEqual(output, "25")
        self.assertIsNone(error)

    def test_03_parentheses(self):
        # Covers: Parentheses
        source = "int x; x = (5 + 10) * 2; print(x);"
        output, error = self.run_interpreter(source)
        self.assertEqual(output, "30")
        self.assertIsNone(error)

    def test_04_real_and_mixed_expressions(self):
        # Covers: real variables, Mixed int and real expressions
        source = "int a; real b; a = 5; b = a + 2.5; print(b);"
        output, error = self.run_interpreter(source)
        self.assertEqual(output, "7.5")
        self.assertIsNone(error)

    def test_05_lexical_error(self):
        # Covers: Lexical error
        source = "int x; x = 10 @ 5;"
        output, error = self.run_interpreter(source)
        self.assertIsNotNone(error)
        self.assertIn("Lexical Error", error)

    def test_06_syntax_error(self):
        # Covers: Syntax error
        source = "int x x = 5;"
        output, error = self.run_interpreter(source)
        self.assertIsNotNone(error)
        self.assertIn("Syntax Error", error)

    def test_07_undeclared_variable(self):
        # Covers: Undeclared variable
        source = "x = 10; print(x);"
        output, error = self.run_interpreter(source)
        self.assertIsNotNone(error)
        self.assertIn("Semantic Error", error)

    def test_08_duplicate_declaration(self):
        # Covers: Duplicate declaration
        source = "int x; real x;"
        output, error = self.run_interpreter(source)
        self.assertIsNotNone(error)
        self.assertIn("Semantic Error", error)

    def test_09_type_error(self):
        # Covers: Type error
        source = "int count; count = 10.5;"
        output, error = self.run_interpreter(source)
        self.assertIsNotNone(error)
        self.assertIn("Semantic Error", error)

    def test_10_division_by_zero(self):
        # Covers: Division by zero
        source = "int x; int y; x = 5; y = x / 0;"
        output, error = self.run_interpreter(source)
        self.assertIsNotNone(error)
        self.assertIn("Runtime Error", error)

    def test_11_uninitialized_variable(self):
        # Covers: Uninitialized variable
        source = "int x; int y; y = x + 5;"
        output, error = self.run_interpreter(source)
        self.assertIsNotNone(error)
        self.assertIn("Semantic Error", error)

if __name__ == '__main__':
    unittest.main()