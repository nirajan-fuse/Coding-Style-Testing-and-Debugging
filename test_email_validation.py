import unittest
from email_validation import validate_email


class Test(unittest.TestCase):
    def setUp(self):
        self.valid_email = [
            "nirajanthakuri@gmail.com",
            "abc.123@yahoo.com",
            "nepal@outlook.com.np",
        ]

        self.invalid_email = [
            "nirajanthakuri",
            "abc.123",
            "nepal@yopmail.com",
        ]

    def test_valid_email(self):
        for email in self.valid_email:
            self.assertTrue(validate_email(email))

    def test_invalid_email(self):
        for email in self.invalid_email:
            self.assertFalse(validate_email(email))


if __name__ == "__main__":
    unittest.main()
