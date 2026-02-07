import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_valid_title(self):
        md = "# Hello\n\nSome text"
        self.assertEqual(extract_title(md), "Hello")

    def test_strips_whitespace(self):
        md = "#   Hello World   "
        self.assertEqual(extract_title(md), "Hello World")

    def test_no_title(self):
        md = "## Subheading"
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()
