from Singleton import Singleton
import urllib2
from bs4 import BeautifulSoup
import re

from ProblemType import Problem_type
from Problem import Problem

CLASSICPROBURL = 'http://www.spoj.com/problems/classical/'
PROBURL = 'http://www.spoj.com/problems/'
SPOJURL = 'http://www.spoj.com'

# @Singleton
class SPOJ_scrapper:

    @staticmethod
    def get_description_from_prob(prob):
        details = SPOJ_scrapper.get_prob_desc(prob)
        # print details
        if (details is None):
            raise Exception("Problem code invalid")

        desc = details[0]
        category_link = details[1]
        problem = Problem(prob, desc, category_link)

        current_page = category_link
        while True:
            response = urllib2.urlopen(current_page)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            prob_link = soup.find('a', href = '/ranks/'+prob)

            if prob_link is not None:
                if problem.type == Problem_type.CLASSICAL:
                    title = prob_link['title']
                    problem.points = title[len('Value '):-len(' points. See the best solutions.')]
                else:
                    problem.points = 0
                problem.solvers = prob_link.text
                return problem
            else:
                next_element = SPOJ_scrapper.get_next_url(soup)
                if next_element is None:
                    raise Exception("Couldn't find problem link")
                current_page = SPOJURL + SPOJ_scrapper.get_next_url(soup)['href']

    @staticmethod
    def get_prob_desc(prob):
        prob_url = PROBURL + prob
        try:
            response = urllib2.urlopen(prob_url)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            name = soup.find('h2', attrs={'id':'problem-name'}).text.strip()
            desc = name[name.find('-')+2:]
            category_link = soup.find('ol', attrs={'class':'breadcrumb'}).findAll('li')[1].find('a')
            return desc, SPOJURL + category_link['href']
        except urllib2.HTTPError:
            print "Can't reach the problem page"
            return None
        except AttributeError:
            print "Invalid problem: ", prob_url
            return None

    @staticmethod
    def get_next_url(current_soup):
        return current_soup.find('a', text='Next', attrs={'class': 'pager_link'})