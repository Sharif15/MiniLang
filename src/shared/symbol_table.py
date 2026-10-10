
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
            raise ValueError(f"Variable '{name}' is not declared.")

        self.symbols[name]["value"] = value
        self.symbols[name]["initialized"] = True

    def get_variable(self, name):
        # Returns the variable's information (type, value, initialized status)
        return self.symbols[name]

    def display_table(self):
        print(f"{'Name':<15} {'Type':<8} {'Initialized':<13} {'Value'}")

        for name, info in self.symbols.items():
            print(
                f"{name:<15} {info['type']:<8} "
                f"{str(info['initialized']):<13} {info['value']}"
            )

    
    def mark_initalized(self, name):
        """
        Marks a declared variable as initialized without assigning a runtime value.

        Used by the semantic analyzer after it verifies
        that an assignment is semantically valid.

        We do this so that the semantic analyzer doesn't assign any
        runtime values, because that should be the interpreter's job.

        Raises a Python KeyError in case something goes
        wrong with OUR code, NOT the MiniLang program code.
        If raised, it indicates our code might have tried to
        manipulate a symbol that should already exist.
        """
        variable = self.get_variable(name)

        if variable is None:
            raise KeyError(f"Cannot mark undeclared variable '{name}' as initialized")

        variable["initialized"] = True


    def reset_runtime_state(self):
        """
        Resets initialization and value information before
        program execution (interpretation) begins.

        Declaration information (name and type) is preserved.

        Again, we do this because the semantic analyzer shouldn't
        be the one assigning runtime values, it should be the interpreter. 
        """
        for variable in self.symbols.values():
            variable["initialized"] = False
            variable["value"] = None
