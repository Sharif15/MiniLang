
class SymbolTable:
    def __init__(self):
        self.symbols = {}
        
    def declare_variable(self, name, var_type):
        # Adds a variable to the table; tracks name, type, and initialized=False
        pass
        
    def assign_value(self, name, value):
        # Updates the value and sets initialized=True
        pass
        
    def get_variable(self, name):
        # Returns the variable's information (type, value, initialized status)
        pass
        
    def display_table(self):
        # Used for the debug/display mode to print the current state
        pass