class ParsingError(Exception):
    """Class indicates a parsing error"""
    def __init__(self, *args) -> None:
        """Called if no parsing pattern fits the string"""
        if len(args) == 0:
            self.msg = "The string does not match any of the patterns for the parsing version"
        else:
            self.msg = " ".join([str(i) for i in args])
    def __str__(self) -> str: return self.msg

class ParsingKeysError(Exception):
    """Class indicates an error when checking compatibility of Version classes"""
    def __init__(self, *args) -> None:
        """Called if the Version class is not compatible with the class with which the comparison was attempted"""
        if len(args) == 0:
            self.msg = "The pattern keys of this class are different from the pattern keys of the other class"
        else:
            self.msg = " ".join([str(i) for i in args])
    def __str__(self) -> str: return self.msg