class MiniLangError(Exception):
    """
    Base class for all user-facing MiniLang Errors
    """
    error_category = "MiniLang"


    def __init__(self, line, message) -> None:
        self.line = line
        self.message = message
        super().__init__(message)


    def __str__(self) -> str:
        return (
            f"{self.error_category} Error on line "
            f"{self.line}: {self.message}"
        )


class LexicalError(MiniLangError):
    error_category = "Lexical"


class MiniLangSyntaxError(MiniLangError):
    error_category = "Syntax"


class SemanticError(MiniLangError):
    error_category = "Semantic"


class MiniLangRuntimeError(MiniLangError):
    error_category = "Runtime"
