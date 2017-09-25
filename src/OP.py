from optparse import OptionParser


class Parser:
    """
    To parse options
    """
    def __init__(self):
        self.parser = OptionParser()
        self.add_all_options()

    def add_all_options(self):
        self.parser.add_option("-p", "--prob", "--problem", action="store",
                               dest="prob", type="string")
        self.parser.add_option("--pid", "--probid", "--problemid",
                               action="store", dest="probid", type="int")
        self.parser.add_option("-c", "--category", action="store",
                               dest="category", type = "string")

    def get_options(self):
        return self.parser.parse_args()
