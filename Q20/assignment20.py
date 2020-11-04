# Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god",
# "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and
# use it to translate your Christmas cards from English into Swedish. That is, write a function translate()
# that takes a list of English words and returns a list of Swedish words.

def Stringconv(inputString):
    dictionaryOfWords = {"merry": "god",
                         "christmas": "jul",
                         "and": "och",
                         'happy': "gott",
                         "new": "nytt",
                         "year": "år"}
    translatedString = ""
    for i in inputString.split(" "):
        if (str(dictionaryOfWords.get(i))) is not None:
            translatedString = translatedString + str(dictionaryOfWords.get(i))
        else:
            translatedString = ""
            return translatedString
    return translatedString


print(Stringconv("merry christmas and happy new year"))
print(Stringconv("merry christmas"))
print(Stringconv("happy new year"))


def Conversion(n):
    dictionaryOfWords = {"merry": "god",
                         "christmas": "jul",
                         "and": "och",
                         'happy': "gott",
                         "new": "nytt",
                         "year": "år"}

    x = n.split()
    c = len(x)
    for i in range(0, c):
        for key, value in dictionaryOfWords.items():
            if key == x[i]:
                print(key + ":" + value)


print(Conversion("merry christmas"))