from ProblemType import Problem_type

class Problem:
    def __init__(self, prob, desc, url):
        self.name = prob
        self.desc = desc
        self.url = url
        self.type = Problem_type.get_type(url)
        self.points = None
        self.solvers = None

    def printDetails(self):
        print 'Description(Full name): ', self.desc
        print 'URL: ', self.url
        print 'Type: ', Problem_type.problem_type_str(self.type)
        print 'Points: ', self.points
        print '#Solvers: ', self.solvers
