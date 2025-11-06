import unittest
from password_analyser import analyse_password

class TestPasswordAnalyser(unittest.TestCase):

    def test_short_password(self):
        result = analyse_password("abc")
        # Expect Weak
        self.assertEqual(result["strength"], "Weak")

    def test_moderate_password(self):
        result = analyse_password("Abcdef12")
        # Expect Moderate
        self.assertEqual(result["strength"], "Moderate")

    def test_strong_password(self):
        result = analyse_password("Abc!1234xyz$")
        # Expect Moderate
        self.assertEqual(result["strength"], "Moderate")

    def test_common_word_password(self):
        result = analyse_password("Password123!")
        # Expect Moderate 
        self.assertEqual(result["strength"], "Moderate")

    def test_repeating_characters(self):
        result = analyse_password("AAAbbb111!!!")
        # Expect Moderate 
        self.assertEqual(result["strength"], "Moderate")

if __name__ == "__main__":
    unittest.main()
