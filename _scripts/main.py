import urllib.request
import nltk

from nltk.corpus import stopwords
from bs4 import BeautifulSoup

def freq_distribution(url):
    freq = nltk.FreqDist(get_clean_tokens(url))
    print(sorted(freq.items(), key=lambda x: x[1]))


def get_clean_tokens(url):
    text = get_content(url)
    tokens = [t for t in text.split()]
    clean_tokens = tokens[:]
    sw = stopwords.words('english')

    for token in tokens:
        if token in sw:
            clean_tokens.remove(token)
    print(clean_tokens)
    return clean_tokens


def get_content(url):
    data = get_webpage(url)
    soup = BeautifulSoup(data, 'html.parser')
    return soup.find('article').get_text()

def get_webpage(url):
    with urllib.request.urlopen(url) as wp:
        data = wp.read()
        return data


def main(url):
    freq_distribution(url)


if __name__ == "__main__":
    main('https://www.optionalrule.com/2021/06/27/gritty-healing-and-survival-rules/')