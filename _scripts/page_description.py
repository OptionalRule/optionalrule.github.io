import urllib.request
import bs4

# I am in the begining stages of adding some natural language options to the blog and this is just play code.

import nltk
import string

from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

LOCAL_STOPWORDS = ['road', '-', 'part', 'join', 'one', 'mile', 'try', 'use', 'new', 'useful', 'use', 'may' 'seem', 'like']

class PageDescription:

    def __init__(self, url):
        """
        Pulls the content from a page off of optional rule and provides some NLTK convience methods.
        """
        self.url = url
        self.raw_page_data = ''
        self.page_content = ''
        self.stopwords = []
        self.clean_tokens = []
        self._extend_stopwords()
        self._get_content()

    def _extend_stopwords(self):
        self.stopwords = stopwords.words('english')
        self.stopwords.extend(map(str, range(10)))
        self.stopwords.extend(LOCAL_STOPWORDS)

    def freq_distribution(self):
        freq = nltk.FreqDist(self.get_clean_tokens())
        return sorted(freq.most_common(5), key=lambda x: x[1], reverse=True)


    def get_clean_tokens(self):
        st = PorterStemmer()
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        tokens = tokenizer.tokenize(self.page_content.lower())
        clean_tokens = [st.stem(t) for t in tokens]

        for token in tokens:
            if token in self.stopwords:
                clean_tokens.remove(st.stem(token))
        self.clean_tokens = clean_tokens
        return clean_tokens


    def _get_content(self):
        self._get_webpage()
        soup = BeautifulSoup(self.raw_page_data, 'html.parser')
        article = soup.find('article')
        if article:
            self.page_content = article.get_text()

    def _get_webpage(self):
        with urllib.request.urlopen(self.url) as wp:
            self.raw_page_data = wp.read()
             
def get_url_list(filepath):
    """
    Reads a local sitemap file to pull out the URLs
    """
    with open(filepath) as f:
        xml = bs4.BeautifulSoup(f.read(), 'lxml-xml')
        return [loc.contents[0] for loc in xml.find_all('loc')]

def page_list(sitemap_path):
    return [PageDescription(url) for url in get_url_list(sitemap_path)]

def main(url):
    page = PageDescription(url)
    print(page.freq_distribution())



if __name__ == "__main__":
    # main('https://www.optionalrule.com/2021/06/27/gritty-healing-and-survival-rules/')
    pages = page_list('docs/sitemap.xml')
    for page in pages:
        print(page.freq_distribution())