import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    #test if equal with URLs
    def test_eq_with_urls(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://www.google.com")
        self.assertEqual(node, node2)

    ## test if not equal with all values different
    def test_not_eq_with_urls(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.google.com")
        node2 = TextNode("This is a different text node", TextType.LINK, "http://www.yahoo.com")
        self.assertNotEqual(node, node2)

    ## test if not equal with no urls
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    ## test not equal only texttype different
    def test_not_eq_text_type_only_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    ## test not equal only texttype different with url
    def test_not_eq_text_type_only_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.google.com")
        node2 = TextNode("This is a text node", TextType.LINK, "http://www.google.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()