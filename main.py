__author__ = 'shreyans800755'

import sys
import op
import scrapper

if __name__ == '__main__':
    parser = op.parser()
    (options, args) = parser.getOptions()
    if options.prob:
        prob = options.prob.upper()
        desc = scrapper.SPOJ_scrapper.get_description_from_prob(prob)
        print 'Points: ', desc[0]
        print '#Solvers: ', desc[1]
