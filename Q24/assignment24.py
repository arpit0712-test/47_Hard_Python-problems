# The third person singular verb form in English is distinguished by the suffix s, which is added to the stem of the
# infinitive form: run runs. A simple set of rules can be given as follows: 1. If the verb ends in y, remove it and
# add ies 2. If the verb ends in o, ch, s, sh, x or z, add es 3. By default just add sYour task in this exercise is
# to define a function make_3sg_form() which given a verb in infinitive form returns its third person singular form.
# Test your function with words like try, brush, run and fix. Note however that the rules must be regarded as
# heuristic, in the sense that you must not expect them to work for all cases. Tip: Check out the string method
# endswith().

def make_3sg_form(str):
    if str.endswith('y'):
        outputStr = str.replace('y', 'ies')
    elif str.endswith('o'):
        outputStr = str.replace('o', 'es')
    elif str.endswith('ch'):
        outputStr = str.replace('ch', 'es')
    elif str.endswith('s'):
        outputStr = str.replace('s', 'es')
    elif str.endswith('sh'):
        outputStr = str.replace('sh', 'es')
    elif str.endswith('x'):
        outputStr = str.replace('x', 'es')
    elif str.endswith('z'):
        outputStr = str.replace('z', 'es')
    else:
        outputStr = str.strip() + 's'

    print(outputStr)


make_3sg_form("scharrch")


def make_3sg_form1(str):
    if str.endswith('y'):
        outputStr = str.strip('y') + 'ies'
    elif str.endswith('o'):
        outputStr = str.strip('o') + 'es'
    elif str.endswith('ch'):
        outputStr = str.strip('ch') + 'es'
    elif str.endswith('s'):
        outputStr = str.strip('s') + 'es'
    elif str.endswith('sh'):
        outputStr = str.strip('sh') + 'es'
    elif str.endswith('x'):
        outputStr = str.strip('x') + 'es'
    elif str.endswith('z'):
        outputStr = str.strip('z') + 'es'
    else:
        outputStr = str.strip() + 's'

    print(outputStr)


make_3sg_form1("fix")