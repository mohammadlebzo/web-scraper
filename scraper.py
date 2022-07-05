import requests
from bs4 import BeautifulSoup
import re


def get_citations_needed_count(url_str):
    """
    This function gets the number of "citation needed" occurrences in a website.
        :param url_str: the URL of the website
        :return: number
    """
    search_word = 'citation needed'
    res = requests.get(url_str)
    soup = BeautifulSoup(res.content, 'html.parser')

    citations = soup.body.find_all(string=re.compile('.*{0}.*'.format(search_word)), recursive=True)

    return len(citations)


def get_citations_needed_report(url_str):
    """
        This function returns the parent tag that contains "citation needed" in the website as text.
            :param url_str: the URL of the website
            :return: list of strings
        """
    search_word = 'citation needed'
    res = requests.get(url_str)
    soup = BeautifulSoup(res.content, 'html.parser')

    paragraphs = soup.find_all("p")

    results = []

    for paragraph in paragraphs:
        if paragraph.find(text=re.compile(search_word)):
            results.append(paragraph.get_text())

    return results


if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    print("The number of \"citation needed\" = ", get_citations_needed_count(url))
    needed_citations_parents = get_citations_needed_report(url)
    for i in needed_citations_parents:
        print('--------------------------------------------\n')
        print(i)
    print('--------------------------------------------')
