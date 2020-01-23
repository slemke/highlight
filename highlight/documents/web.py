from highlight.documents.normalize import normalize
import bs4 as BeautifulSoup
import urllib.request


def fetch(url):
    response = urllib.request.urlopen(url)
    article = response.read().decode('utf8')
    parsed_article = BeautifulSoup.BeautifulSoup(article, 'html.parser')
    text = find_content(parsed_article)
    return normalize(text)


def find_content(article):
    tags = article.body.find_all(has_content)
    return get_text_from_largest_tag(tags)


def has_content(tag):
    children = tag.findChildren('p', recursive=False)
    t = [x for x in children if x]
    return len(t) > 0


def get_text_from_largest_tag(tags):
    top_length = 1
    element = ''
    for tag in tags:
        text_length = len(tag.get_text())
        if text_length > top_length:
            top_length = text_length
            element = tag
    return element.get_text()
