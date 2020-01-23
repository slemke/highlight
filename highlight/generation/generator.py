from html import escape
from highlight.file import read, write
from operator import itemgetter


def generate_output(document, path):
    template = read('generation/template/index.html')
    content = ""
    median = calculate_median(document)
    for sentences in document:
        if sentences['weight'] > median:
            content += '<span class="highlight">'
        else:
            content += '<span>'
        content += ' ' + escape(sentences['text'])

        content += "</span>"
    template = template.replace('{{ content }}', content)

    write(path, template)


def calculate_median(sentences):
    sorted_sentences = sorted(sentences, key=itemgetter('weight'))
    number_of_sentences = len(sorted_sentences)

    if number_of_sentences % 2 == 0:
        median = int(number_of_sentences / 2 - 1)
    else:
        median = int((number_of_sentences - 1) / 2 - 1)

    return sorted_sentences[median]['weight']
