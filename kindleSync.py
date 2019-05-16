from tinycards import Tinycards
from tinycards.model import Deck
from PyDictionary import PyDictionary
import yaml, json, sys
import config  

dictionary=PyDictionary()
tinycards = Tinycards(config.TINY_CARDS_CREDENTIALS['email'], config.TINY_CARDS_CREDENTIALS['password'])    
deck = Deck('12 Rules Of Life')
deck = tinycards.create_deck(deck)
fh = open('words.txt')
for word in fh:    
    meaning = str(dictionary.meaning(word))
    translation_table = dict.fromkeys(map(ord, '{}[]\''), None)
    meaning = meaning.translate(translation_table)
    print(meaning)
    deck.add_card((word, meaning))
fh.close()

tinycards.update_deck(deck)




