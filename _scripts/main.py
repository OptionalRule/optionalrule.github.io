import urllib.request
# I am in the begining stages of adding some natural language options to the blog and this is just play code.

import nltk

from nltk.corpus import stopwords
from bs4 import BeautifulSoup

class PageDescription:

    def __init__(self, url):
        """
        Pulls the content from a page off of optional rule and provides some NLTK convience methods.
        """
        self.url = url
        self.raw_page_data = None
        self.page_content = None
        self._get_content()

    def freq_distribution(self):
        freq = nltk.FreqDist(self.get_clean_tokens())
        return sorted(freq.most_common(5), key=lambda x: x[1], reverse=True)


    def get_clean_tokens(self):
        tokens = [t.lower() for t in self.page_content.split()]
        clean_tokens = tokens[:]
        sw = stopwords.words('english')

        for token in tokens:
            if token in sw:
                clean_tokens.remove(token)
        return clean_tokens


    def _get_content(self):
        self._get_webpage()
        soup = BeautifulSoup(self.raw_page_data, 'html.parser')
        self.page_content = soup.find('article').get_text()

    def _get_webpage(self):
        with urllib.request.urlopen(self.url) as wp:
            self.raw_page_data = wp.read()
             

def main(url):
    page = PageDescription(url)
    print(page.freq_distribution())


if __name__ == "__main__":
    main('https://www.optionalrule.com/2021/06/27/gritty-healing-and-survival-rules/')