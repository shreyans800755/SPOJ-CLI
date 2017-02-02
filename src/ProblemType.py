class Problem_type:
    types = ['', 'CLASSICAL', 'CHALLENGE', 'PARTIAL', 'TUTORIAL', 'RIDDLE', 'BASICS']

    CLASSICAL = 1
    CHALLENGE = 2
    PARTIAL = 3
    TUTORIAL = 4
    RIDDLE = 5
    BASICS = 6

    @staticmethod
    def problem_type_str(type):
        return Problem_type.types[type]

    @staticmethod
    def get_type(type_str):
        for i in range(1, len(Problem_type.types)):
            if Problem_type.types[i] in type_str.upper():
                return i
        return 0
