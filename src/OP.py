from optparse import OptionParser

class Parser:
    """
    To parse options
    """
    def __init__(self):
        self.parser = OptionParser()
        self.addAllOptions()

    def addAllOptions(self):
        self.parser.add_option("-p", "--prob", "--problem", action = "store", dest = "prob", type = "string")
        self.parser.add_option("--pid", "--probid", "--problemid", action = "store", dest = "probid", type = "int")

    def getOptions(self):
        return self.parser.parse_args()
