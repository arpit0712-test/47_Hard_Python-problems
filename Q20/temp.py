def ConversionStr(inputString):
    dictionaryOfWords = {"merry": "god",
                         "christmas": "jul",
                         "and": "och",
                         'happy': "gott",
                         "new": "nytt",
                         "year": "år"}
    translatedString = ""
    for i in inputString.split(" "):
        if (dictionaryOfWords.get(i)) is not None:
            translatedString = translatedString + dictionaryOfWords.get(i)
        else:
            translatedString = ""
            return translatedString
    return translatedString


print(ConversionStr("merry christmas"))