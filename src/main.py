#!/usr/bin/env python3

import OP
import Scrapper

__author__ = 'shreyans800755'

if __name__ == '__main__':
    parser = OP.Parser()
    (options, args) = parser.get_options()
    # pdb.set_trace()
    if options.prob:
        prob = options.prob.upper()
        try:
            problem = Scrapper.SPOJScrapper.get_problem(prob)
            problem.printDetails()
        except Exception as e:
            print(e)

    if options.probid:
        probid = options.probid
        try:
            problem = Scrapper.SPOJScrapper.get_problem_from_id(probid)
            problem.printDetails()
        except Exception as e:
            print(e)