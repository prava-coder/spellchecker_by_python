#import spellchecker package
from spellchecker import SpellChecker
spell=SpellChecker()
#find the words that may be misspelled
misspelled=spell.unknown(["fop","fivl","give","f4rever"])
#to get the correct spell
for word in misspelled:
    print(spell.correction(word))