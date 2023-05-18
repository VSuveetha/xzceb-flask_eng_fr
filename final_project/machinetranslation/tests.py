import unittest

from translator import englishtofrench, englishtogerman

class TestEnglishtofrench(unittest.TestCase):
    '''Tests English to French function'''
    def test1(self):
        '''Tests null, hello and snake translations'''
        self.assertEqual(englishToFrench(None), '')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench('snake'), 'serpent')

class TestFrenchtoenglish(unittest.TestCase):
    '''Tests French to English function'''
    def test1(self):
        '''Tests null, hello and snake translations'''
        self.assertEqual(frenchToEnglish(None), '')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish('serpent'), 'snake')

unittest.main()