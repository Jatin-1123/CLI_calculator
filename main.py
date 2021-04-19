import math
import re
from typing import *


class Parser:

    def __init__(self, expression: str) -> None:

        self.patterns = {
            "Perm": re.compile(r"(\([0-9]+\)|[0-9]+)[Pp](\([0-9]+\)|[0-9]+)"),
            "Comb": re.compile(r"(\([1-9]+\)|[0-9]+)[Cc](\([0-9]+\)|[0-9]+)"),
            "sqrt": re.compile(r"sqrt\(([0-9]+)\)"),
        }

        self.exp: str = expression
        self.exp = re.sub(r'[\[{]', '(', self.exp)  # Replacing all Brackets to Paranthesis (LEFT)
        self.exp = re.sub(r'[]}]', ')', self.exp)  # Replacing all Brackets to Paranthesis (RIGHT)
        self.exp = re.sub(r'\s', '', self.exp)  # Removing ALL Whitespaces (to make it easier for parser)
        self.exp = re.sub(r"^\((.*)\)$", lambda m: m.group(1), self.exp)  # Removing the enclosing brackets (REDUNDANT)

        self.validExpression: bool = self.validate()

    def validate(self) -> bool:
        try:
            assert (re.search(r"([0-9PpCc()+-/*]|sqrt)*", self.exp).group(0) == self.exp)
            assert (self.exp.count('(') == self.exp.count(')'))
            return True
        except AssertionError:
            print("INVALID EXPRESSION")
            return False

    def evaluate(self, subExp: Optional[str] = None) -> Union[int, float]:
        code = f"result = {subExp}" if subExp else f"result = {self.exp}"
        loc = {}
        exec(code, globals(), loc)
        return loc['result']

    def parse(self) -> None:
        def sqrt_replace(m: re.match) -> str: return f"{math.sqrt(m.group(1))}"

        def perm_replace(m: re.match) -> str:
            return m.group(1)

        self.exp = re.sub(pattern=self.patterns["sqrt"], repl=sqrt_replace, string=self.exp)
        self.exp = re.sub(pattern=self.patterns["perm"], repl=perm_replace, string=self.exp)
        self.exp = re.sub(pattern=self.patterns["sqrt"], repl=sqrt_replace, string=self.exp)


if __name__ == '__main__':
    pass
