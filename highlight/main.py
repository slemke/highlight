from highlight.documents.web import fetch
from highlight.nlp.nlp import parse, score
from highlight.generation.generator import generate_output


def main():
    article = fetch("https://docs.python-guide.org/writing/structure/#structure-of-code-is-key")
    document = parse(article)
    document = score(document)
    generate_output(document, 'output.html')


if __name__ == "__main__":
    main()
