class ProblemType:
    types = ['', 'CLASSICAL', 'CHALLENGE', 'PARTIAL', 'TUTORIAL', 'RIDDLE', 'BASICS']

    CLASSICAL = 1
    CHALLENGE = 2
    PARTIAL = 3
    TUTORIAL = 4
    RIDDLE = 5
    BASICS = 6

    @staticmethod
    def get_type_str(type):
        return ProblemType.types[type]

    @staticmethod
    def get_type(type_str):
        for i in range(1, len(ProblemType.types)):
            if ProblemType.types[i] in type_str.upper():
                return i
        return 0
