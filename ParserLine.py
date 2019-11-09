class ParserException(Exception):
    pass


class ParserLine:
    def __init__(self, line):
        if isinstance(line, str):
            self.line = line
        else:
            raise ParserException("Error in parse line")

    def getObjectFromLine(self):
        pass