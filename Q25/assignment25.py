# In English, the present participle is formed by adding the suffix ing to the infinite form: go -> going. A simple
# set of heuristic rules can be given as follows:
# 1. If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
# 2. If the verb ends in ie, change ie to y and add ing
# 3. For words consisting of consonant vowel consonant, double the final letter before adding ing
# 4. By default just add ing
# Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form
# returns its present participle form. Test your function with words such as lie, see, move and hug. However,
# you must not expect such simple rules to work for all cases.

def make_ing_form(str):
    if str.endswith('e'):
        outputStr = str.replace('e', 'ing')
    elif str.endswith('ie'):
        outputStr = str.replace('ie', 'y'+'ing')
    elif str.endswith('ch'):
        outputStr = str.replace('ch', 'es')
    else:
        outputStr = str.strip() + 'ing'

    print(outputStr)


# make_ing_form("hug")
# make_ing_form("see")
# make_ing_form("lie")
# make_ing_form("move")
# make_ing_form("say")
# make_ing_form("give")


def make_ing_form1(str):
    if str.endswith('e'):
        outputStr = str.strip('e') + 'ing'
    elif str.endswith('ie'):
        outputStr = str.strip('ie') + 'y'+'ing'
    elif str.endswith('ch'):
        outputStr = str.strip('ch') + 'es'
    else:
        outputStr = str.strip() + 'ing'
    print(outputStr)


make_ing_form1("switch")
