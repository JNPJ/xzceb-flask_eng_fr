from translator import english_to_french, french_to_english
import unittest

class test_translator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french(0), 0)

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english(0), 0)

if __name__ == '__main__':
    unittest.main()

