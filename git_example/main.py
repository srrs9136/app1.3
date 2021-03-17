from greetings import greet
from translate import Translator

translator = Translator(to_lang='pt')
for g in greet:
    print(translator.translate(g).title())