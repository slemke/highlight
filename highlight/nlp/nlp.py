import nltk


def parse(text):
    text_elements = split_text(text)
    tokenized_sentences = []
    for elements in text_elements:
        sentences = nltk.sent_tokenize(elements)
        for sentence in sentences:
            s = {
                'token': nltk.word_tokenize(sentence),
                'text': sentence
            }
            tokenized_sentences.append(s)
    return tokenized_sentences


def split_text(text):
    split = text.split('\n\n')
    text_elements = []
    for s in split:
        text_elements.append(s.replace('\n', ' ').strip())
    return text_elements


def score(sentences):
    frequency = count_word_frequency(sentences)
    return weigh_sentences(sentences, frequency)


def count_word_frequency(sentences):
    frequency = dict()
    for sentence in sentences:
        for token in sentence['token']:
            if token in frequency:
                frequency[token] += 1
            else:
                frequency[token] = 1
    return weight_frequency(frequency)


def weight_frequency(frequency):
    max_frequency_key = max(frequency, key=frequency.get)
    max_frequency = frequency[max_frequency_key]
    for key in frequency:
        frequency[key] = frequency[key] / max_frequency
    return frequency


def weigh_sentences(sentences, frequency):
    weight_sentences = []
    for sentence in sentences:
        s = {
            'token': sentence['token'],
            'text': sentence['text'],
            'length': len(sentence)
        }
        weight = 0.0
        for token in sentence['token']:
            weight += frequency[token]
        s['weight'] = weight / s['length']
        weight_sentences.append(s)
    return weight_sentences
