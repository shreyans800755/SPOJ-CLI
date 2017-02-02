#!/usr/bin/env python

__author__ = 'shreyans800755'

import sys
import OP
import Scrapper
import pdb

if __name__ == '__main__':
    parser = OP.Parser()
    (options, args) = parser.getOptions()
    # pdb.set_trace()
    if options.prob:
        prob = options.prob.upper()
        try:
            problem = Scrapper.SPOJ_scrapper.get_description_from_prob(prob)
            problem.printDetails()
        except Exception as e:
            print e