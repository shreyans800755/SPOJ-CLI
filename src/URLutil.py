from ProblemType import *

PROBURL = 'http://www.spoj.com/problems/'
SPOJURL = 'http://www.spoj.com'


def get_problems_url(type):
    return PROBURL + ProblemType.get_type_str(type).lower()