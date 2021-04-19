import re


class Parser:
    patterns = [
        re.compile(r"(\([0-9]+\)|[0-9]+)[Pp](\([0-9]+\)|[0-9]+)"),
        re.compile(r"(\([1-9]+\)|[0-9]+)[Cc](\([0-9]+\)|[0-9]+)"),
        re.compile(r"sqrt\([0-9]+\)"),
    ]

    def __init__(self, expression: str) -> None:
        self.exp: str = expression
        self.validExpression: bool = self.validate()

    def validate(self) -> bool:
        if re.search(r"([0-9PpCc() +-/*]|sqrt)*", self.exp).group(0) != self.exp:
            print("INVALID EXPRESSION")
            return False
        return True

    def eval(self, subExp: str):
        pass

    def parse(self) -> None:
        pass


if __name__ == '__main__':
    pass
