from dataclasses import dataclass, field

# AST Node Definitions

@dataclass
class Program:
    statements: list = field(default_factory=list)
    line: int = 1


@dataclass
class Declaration:
    var_type: str
    name: str
    line: int


@dataclass
class Assignment:
    name: str
    expression: object
    line: int


@dataclass
class PrintStatement:
    expression: object
    line: int


@dataclass
class Identifier:
    name: str
    line: int


@dataclass
class IntegerLiteral:
    value: int
    line: int


@dataclass
class RealLiteral:
    value: float
    line: int


@dataclass
class BinaryExpression:
    left: object
    operator: str
    right: object
    line: int