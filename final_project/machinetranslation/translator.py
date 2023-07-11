"""
imports MyMemoryTranslator from the deep_translator
"""
from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """
    function english_to_french and converts english to french 
    """
    new_translated = MyMemoryTranslator(source='english', target='french').translate(english_text)
    french_text= new_translated[0:7]
    return french_text


def french_to_english(french_text):
    """
    function french_to_english and converts french to english 
    """
    new_translated = MyMemoryTranslator(source= 'french', target= 'english' ).translate(french_text)
    english_text= new_translated[0:7]
    return english_text
