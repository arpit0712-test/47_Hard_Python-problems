# A sentence splitter is a program capable of splitting a text into sentences. The standard set of heuristics for
# sentence splitting includes (but isn't limited to) the following rules:
# Sentence boundaries occur at one of "." (periods), "?" or "!", except that
# 1. Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
# 2. Periods followed by a digit with no intervening whitespace are not sentence boundaries.
# 3. Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles
# are not sentence boundaries. Sample titles include Mr., Mrs., Dr., and so on.
# 4. Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries (for
# example, www.aptex.com, or e.g).
# 5. Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not
# sentence boundaries.
# Your task here is to write a program that given the name of a text file is able to write its content with each
# sentence on a separate line.

import re


def sentence_splitter(file_name):
    with open(file_name, 'r') as f:
        file_content = f.read()

    sentences = re.sub(r'\n', '', file_content)
    sentences = re.sub(r'(?<!Mr>)(?<!Mrs>)(?<!Dr>)\.\s([A-Z])', r'.\n\1', sentences)
    sentences = re.sub(r'!\s', '!\n', sentences)
    sentences = re.sub(r'\?\s', '?\n', sentences)
    print(sentences)


sentence_splitter('splitter.text')
