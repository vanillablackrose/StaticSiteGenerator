import unittest

from nodeparsing import extract_markdown_images, extract_markdown_links

class TestNodeExtractLinkImage(unittest.TestCase):
    def test_image(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_link(self):
        matches = extract_markdown_links("This is text with an [link](http://www.google.com)")
        self.assertListEqual([("link", "http://www.google.com")], matches)

    def test_no_image(self):
        matches = extract_markdown_images("This is text with no image ")
        self.assertListEqual([], matches)

    def test_no_link(self):
        matches = extract_markdown_links("This is text with no link")
        self.assertListEqual([], matches)    


if __name__ == "__main__":
    unittest.main()