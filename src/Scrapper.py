from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

from ProblemType import ProblemType
from Problem import Problem
import URLutil


class SPOJScrapper:

    @staticmethod
    def get_problem(prob):
        details = SPOJScrapper.get_prob_desc(prob)
        # print details
        if details is None:
            raise Exception("Problem code invalid")

        desc = details[0]
        category_link = details[1]
        problem = Problem(prob, desc, category_link)

        current_page = category_link
        while True:
            response = urlopen(current_page)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            prob_link = soup.find('a', href = '/ranks/'+prob)

            if prob_link is not None:
                SPOJScrapper.set_points_and_solvers(problem, prob_link)
                return problem
            else:
                next_element = SPOJScrapper.get_next_url(soup)
                if next_element is None:
                    raise Exception("Couldn't find problem link")
                current_page = URLutil.SPOJURL + SPOJScrapper.get_next_url(soup)['href']

    @staticmethod
    def get_problem_from_id(probid):
        for category in range(1, len(ProblemType.types)):
            category_link = URLutil.get_problems_url(category)
            current_page = category_link
            while True:
                response = urlopen(current_page)
                html = response.read()
                soup = BeautifulSoup(html, 'html.parser')
                # TODO: Complete this method

    @staticmethod
    def get_prob_desc(prob):
        problem_url = URLutil.PROBURL + prob
        try:
            response = urlopen(problem_url)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            name = soup.find('h2', attrs = {'id':'problem-name'}).text.strip()
            desc = name[name.find('-')+2:]
            category_link = soup.find('ol', attrs = {'class':'breadcrumb'}).findAll('li')[1].find('a')
            return desc, URLutil.SPOJURL + category_link['href']
        except HTTPError:
            print("Can't reach the problem page")
            return None
        except AttributeError:
            print("Invalid problem: ", problem_url)
            return None

    @staticmethod
    def get_next_url(current_soup):
        return current_soup.find('a', text='Next', attrs={'class': 'pager_link'})

    @staticmethod
    def set_points_and_solvers(problem, prob_link):
        if problem.type == ProblemType.CLASSICAL:
            title = prob_link['title']
            problem.points = title[len('Value '):-len(' points. See the best solutions.')]
        else:
            problem.points = 0
        problem.solvers = prob_link.text