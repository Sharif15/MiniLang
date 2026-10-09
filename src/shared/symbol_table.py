
class SymbolTable:
    def __init__(self):
        self.symbols = {}
        
    def declare_variable(self, name, var_type):
        # Adds a variable to the table; tracks name, type, and initialized=False
        if name in self.symbols:
            raise ValueError(f"Variable '{name}' is already declared.")

        self.symbols[name] = { "type": var_type, "initialized": False, "value": None }

    def assign_value(self, name, value):
        # Updates the value and sets initialized=True
        if name not in self.symbols:
            raise ValueError(f"Semantic Error: Variable '{name}' is not declared.")

        self.symbols[name]["value"] = value
        self.symbols[name]["initialized"] = True
        
    def get_variable(self, name):
        # Returns the variable's information (type, value, initialized status)
        if name not in self.symbols:
                    raise ValueError(f"Semantic Error: Variable '{name}' is not declared.")
        return self.symbols[name]
        
    def display_table(self):
        print(f"{'Name':<15} {'Type':<8} {'Initialized':<13} {'Value'}")

        for name, info in self.symbols.items():
            print(
                f"{name:<15} {info['type']:<8} "
                f"{str(info['initialized']):<13} {info['value']}"
            )