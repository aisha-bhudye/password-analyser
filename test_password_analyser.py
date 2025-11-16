import unittest
from password_checker import analyse_password


class TestPasswordAnalyser(unittest.TestCase):

    def test_short_password(self):
        result = analyse_password("abc" , set())
        # Expect Weak
        self.assertEqual(result["strength"], "Weak")

    def test_moderate_password(self):
        result = analyse_password("Abcdef12" , set())
        # Expect Moderate
        self.assertEqual(result["strength"], "Moderate")

    def test_strong_password(self):
        result = analyse_password("Abc!1234xyz$" , set())
        # Expect Moderate
        self.assertEqual(result["strength"], "Moderate")

    def test_common_word_password(self):
        result = analyse_password("Password123!" , set())
        # Expect Moderate 
        self.assertEqual(result["strength"], "Moderate")

    def test_repeating_characters(self):
        result = analyse_password("AAAbbb111!!!" , set())
        # Expect Moderate 
        self.assertEqual(result["strength"], "Moderate")

if __name__ == "__main__":
    unittest.main()
