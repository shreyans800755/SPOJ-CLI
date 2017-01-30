from Singleton import Singleton
import urllib2
from bs4 import BeautifulSoup
import re

CLASSICPROBURL = 'http://www.spoj.com/problems/classical/'
PROBURL = 'http://www.spoj.com/problems/'
SPOJURL = 'http://www.spoj.com'

# @Singleton
class SPOJ_scrapper:

    @staticmethod
    def get_description_from_prob(prob):
        details = SPOJ_scrapper.get_prob_desc(prob)
        # print details
        if details is None:
            raise Exception("Problem code invalid")
        response = urllib2.urlopen(details[1])
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        prob_link = soup.find('a', href = '/ranks/'+prob)

        title = prob_link['title']

        points = title[len('Value '):-len(' points. See the best solutions.')]
        solvers = prob_link.text
        return (points, solvers)

    @staticmethod
    def get_prob_desc(prob):
        prob_url = PROBURL + prob
        try:
            response = urllib2.urlopen(prob_url)
            # print prob_url
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