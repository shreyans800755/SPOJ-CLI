from ProblemType import ProblemType

class Problem:
    def __init__(self, prob, desc, url, number = None):
        self.number = number
        self.name = prob
        self.desc = desc
        self.url = url
        self.type = ProblemType.get_type(url)
        self.points = None
        self.solvers = None

    def printDetails(self):
        print('Description(Full name): ', self.desc)
        print('URL:', self.url)
        print('Type:', ProblemType.get_type_str(self.type))
        print('Points:', self.points)
        print('#Solvers:', self.solvers)
