from translator import english_to_french,french_to_english
import unittest

class testenfr(unittest.TestCase):
    def test_eng_fr(self):
        self.assertEqual(english_to_french('boy'),'garçon')
        self.assertNotEqual(english_to_french('School'),'Lecole')

class testfren(unittest.TestCase):
    def test_fr_eng(self):
        self.assertEqual(french_to_english('garçon'),'boy')
        self.assertNotEqual(french_to_english('Fleur'),'Flow')

unittest.main()