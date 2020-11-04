# Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god",
# "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and
# use it to translate your Christmas cards from English into Swedish. Use the higher order function map() to
# write a function translate() that takes a list of English words and returns a list of Swedish words

def translate(sourceStr):
    dict1 = {"merry": "god",
             "christmas": "jul",
             "and": "och",
             "happy": "gott",
             "new": "nytt",
             "year": "år"}
    listOfwords = ""
    for word in sourceStr.split(" "):
        if str(dict1.get(word)) is not None:
            listOfwords = listOfwords + str(dict1.get(word))
        else:
            listOfwords = ""
            return listOfwords
    return listOfwords


sourceStr = "merry christmas"
print(translate(sourceStr))


def map_of(words):
    dict1 = {"merry": "god",
             "christmas": "jul",
             "and": "och",
             "happy": "gott",
             "new": "nytt",
             "year": "år"}
    return map(lambda word: dict1[word], words)


words = ["merry","christmas"]
print(list(map_of(words)))
