from highlight.documents.web import fetch
from highlight.nlp.nlp import parse, score
from highlight.generation.generator import generate_output
import sys


def main():
    article = fetch(sys.argv[1])
    document = parse(article)
    document = score(document)
    generate_output(document, 'output.html')


if __name__ == "__main__":
    main()
