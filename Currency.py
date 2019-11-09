import csv
from ParserLine import  ParserLine
from ParserLine import  ParserException

class CurrencyParser(ParserLine):

    def __init__(self, line, delimiter):
        super().__init__(line)
        self.delimiter = delimiter

    def getObjectFromLine(self):
        try:
            parser = csv.reader([self.line], delimiter=self.delimiter)
            values = list(parser)
            iid = int(values[0][0])
            name = str(values[0][1])
            buyValue = int(float(values[0][2]))
            saleValue = int(float(values[0][3]))
            return Currency(iid, name, buyValue, saleValue)
        except Exception as e:
            raise ParserException("Error parser values in line: "+str(e))


class CurrencyFactory:
    
    @staticmethod
    def build(line):
        try:
            cparser = CurrencyParser(line, ',')
            return cparser.getObjectFromLine()
        except ParserException as e:
            raise ParserException(str(e))

    @staticmethod
    def buildFromFile(file):
        try:
            list = []
            with open(file) as csv_file:
                for line in csv_file:
                    try:
                        list.append(CurrencyFactory.build(line))
                    except ParserException:
                        pass

            return list
        except Exception as e:
               print(str(e))   


class Currency:

    def __init__(self, iid, name, buyValue, saleValue):
        self.iid = iid
        self.name = name
        self.buyValue = buyValue
        self.saleValue = saleValue

    def __str__(self):
        return "Currency{" + "id: " + str(self.iid) +  ", name: " + self.name + ", buyValue: " + str(self.buyValue) + ", saleValue: " + str(self.saleValue) + "}"