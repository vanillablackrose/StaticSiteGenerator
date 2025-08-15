import unittest

from textnode import TextNode, TextType
from nodeparsing import split_nodes_delimiter

class TestNodeDelimiterSplit(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text with only text nodes in the node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        total = len(new_nodes)
        self.assertEqual(total, 1)

    def test_bold(self):
        node = TextNode("This is a text with **a bold node here** in the node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        total = len(new_nodes)
        self.assertEqual(total, 3)

    def test_italic(self):
        node = TextNode("This is a text with _an italic node here_ in the node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        total = len(new_nodes)
        self.assertEqual(total, 3)

    def test_code(self):
        node = TextNode("This is a text with `a code node here` in the node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        total = len(new_nodes)
        self.assertEqual(total, 3)

    def test_bold_and_italic(self):
        node = TextNode("This is a text with **a bold node here** _and italic node here_ in the node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"**", TextType.BOLD)
        new_nodes_italic = split_nodes_delimiter(new_nodes,"_", TextType.ITALIC)
        total = len(new_nodes_italic)
        self.assertEqual(total, 5)

    def test_invalid_type(self):
        node = TextNode("This is a text with **a bold node here in the node that is broken!", TextType.TEXT)
        self.assertRaises(ValueError, split_nodes_delimiter, [node], "**", TextType.BOLD)


if __name__ == "__main__":
    unittest.main()