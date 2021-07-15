import nltk
import string
import os

from urllib.parse import urlparse
from nltk.stem import porter
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.parse.generate import generate, demo_grammar
from bs4 import BeautifulSoup

LOCAL_STOPWORDS = [
    "road",
    "-",
    "part",
    "join",
    "one",
    "mile",
    "try",
    "use",
    "new",
    "useful",
    "use",
    "may", 
    "seem",
    "like",
    "way",
    "get"
]


class TextDescription:
    def __init__(self, filepath):
        """
        Pulls the content from a page off of optional rule and provides some NLTK convience methods.
        """
        self.filepath = filepath
        self.text_content = ""
        self.stopwords = extended_stopwords()
        self.clean_tokens = []
        self._get_text()

    def freq_distribution(self, num):
        freq = nltk.FreqDist(self.get_clean_tokens())
        return sorted(freq.most_common(num), key=lambda x: x[1], reverse=True)

    def get_clean_tokens(self):
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        lemma = nltk.WordNetLemmatizer()
        tokens = [lemma.lemmatize(t) for t in tokenizer.tokenize(self.text_content.lower())]
        clean_tokens = [t for t in tokens]

        for token in tokens:
            if token in self.stopwords:
                clean_tokens.remove(token)
        self.clean_tokens = clean_tokens
        return clean_tokens

    def _get_text(self):
        with open(self.filepath, encoding='utf8') as f:
            self.text_content = f.read()


class PageDescription:
    def __init__(self, url, basedir):
        """
        Pulls the content from a page off of optional rule and provides some NLTK convience methods.
        """
        self.url = url
        self.basedir = basedir
        self.raw_page_data = ""
        self.text_content = ""
        self.stopwords = extended_stopwords()
        self.clean_tokens = []
        self._set_raw_data()
        self._set_content()

    def freq_distribution(self):
        freq = nltk.FreqDist(self.get_clean_tokens())
        return sorted(freq.most_common(5), key=lambda x: x[1], reverse=True)

    def get_clean_tokens(self):
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        tokens = tokenizer.tokenize(self.content.lower())
        clean_tokens = [t for t in tokens]

        for token in tokens:
            if token in self.sw:
                clean_tokens.remove(token)
        self.clean_tokens = clean_tokens
        return clean_tokens

    def _set_content(self):
        soup = BeautifulSoup(self.raw_page_data, "html.parser")
        article = soup.find("article")
        if article:
            self.text_content = article.get_text()

    def _set_raw_data(self):
        with open(self.basedir + urlparse(self.url).path + "index.html", "rb") as f:
            self.raw_page_data = f.read()


class PageCollection:
    def __init__(self, pages):
        self.pages = pages
        self._aggregate_content()

    def _aggregate_content(self):
        self.content = " ".join([p.text_content for p in self.pages])

    def get_clean_tokens(self):
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        tokens = tokenizer.tokenize(self.content.lower())
        clean_tokens = [t for t in tokens]

        for token in tokens:
            if token in extended_stopwords():
                clean_tokens.remove(token)
        self.clean_tokens = clean_tokens
        return clean_tokens

    def freq_distribution(self, n=10):
        freq = nltk.FreqDist(self.get_clean_tokens())
        return sorted(freq.most_common(n), key=lambda x: x[1], reverse=True)



def extended_stopwords():
    sw = stopwords.words("english")
    sw.extend(map(str, range(10)))
    sw.extend(LOCAL_STOPWORDS)
    return sw


def get_url_list_from_sitemap(filepath):
    """
    Reads a local sitemap file to pull out the URLs
    """
    with open(filepath, "rb") as f:
        xml = BeautifulSoup(f.read(), "lxml-xml")
        return [loc.contents[0] for loc in xml.find_all("loc")]


def get_post_list(basedir, url_list):
    post_list = []
    for url in url_list:
        if urlparse(url).path.startswith("/202"):
            post_list.append(PageDescription(url, basedir))
    return post_list


def main(url):
    pass


if __name__ == "__main__":
    phb = TextDescription('_scripts/data/phbtext.txt')
    for item in phb.freq_distribution(52):
        print(f"{item[0]}, {item[1]}")
