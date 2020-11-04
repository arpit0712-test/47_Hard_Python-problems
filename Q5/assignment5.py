# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's
# language"). That is, double every consonant and place an occurrence of "o" in between. For example,
# translate("this is fun") should return the string "tothohisos isos fofunon"

def character_Search(chr):
    if (chr.__eq__('a') | (chr.__eq__('A'))) | (chr.__eq__('e') | (chr.__eq__('E'))) | (
            chr.__eq__('i') | (chr.__eq__('I'))) | (chr.__eq__('o') | (chr.__eq__('O'))) | (
            chr.__eq__('u') | (chr.__eq__('U'))):
        return True
    else:
        return False


def translate(strTranslate):
    translated_str = ""
    for i in strTranslate:
        if character_Search(i) == True or str(i) == " ":
            translated_str = translated_str + str(i)
        elif character_Search(i) == False:
            translated_str = translated_str + str(i) + "o" + str(i)
    return translated_str


print(str(translate("this is fun")))


def translate2(translateString):
    vowelsList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_string = ""
    for i in translateString:
        if i in vowelsList or str(i) == " ":
            new_string = new_string + str(i)
        else:
            new_string = new_string + str(i) + "o" + str(i)
    return new_string


print(str(translate2("The quick brown fox jumped on the lazy dog")))
