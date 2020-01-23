def read(path):
    f = open(path, encoding='utf8')
    return f.read()


def write(path, content):
    f = open(path, "w", encoding='utf8')
    f.write(content)
    f.close()
