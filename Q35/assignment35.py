# The International Civil Aviation Organization (ICAO) alphabet assigns code words to the letters of the
# English alphabet acrophonically (Alfa for A, Bravo for B, etc.) so that critical combinations of letters (and
# numbers) can be pronounced and understood by those who transmit and receive voice messages by radio
# or telephone regardless of their native language, especially when the safety of navigation or persons is
# essential. Here is a Python dictionary covering one version of the ICAO alphabet:
# Your task in this exercise is to write a procedure speak_ICAO() able to translate any text (i.e. any string)
# into spoken ICAO words. You need to import at least two libraries: os and time. On a mac, you have
# access to the system TTS (TextToSpeech) as follows: os.system('say ' + msg), where msg is the
# string to be spoken. (Under UNIX/Linux and Windows, something similar might exist.) Apart from the text to
# be spoken, your procedure also needs to accept two additional parameters: a float indicating the length of
# the pause between each spoken ICAO word, and a float indicating the length of the pause between each
# word spoken.
import os
import re

from gtts import gTTS


def speak_ICAO(string):
    d = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
         'f': 'foxtrot',
         'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett', 'k': 'kilo',
         'l': 'lima',
         'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa', 'q': 'quebec',
         'r': 'romeo',
         's': 'sierra', 't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey',
         'x': 'x-ray', 'y': 'yankee', 'z': 'zulu'}
    translated = ""
    for word in (re.findall('[a-zA-Z0-9?!]+', string)):
        for j in range(len(word)):
            if word[j] in d:
                translated = translated + d[word[j]]
            else:
                translated = translated + word[j]
        translated = translated + " "
    tts = gTTS(text=translated, lang='en')
    os.system('say ' + translated)
    tts.save("test.mp3")
    os.system("mpg321 test.mp3 -quiet")


print(speak_ICAO("a.......b.......c......d.......e......f......g.....h......i......j"))
print(speak_ICAO("k.......l.......m......n.......o......p......q.....r......s"))
print(speak_ICAO("t.......u.......v......w.......x......y......z"))
