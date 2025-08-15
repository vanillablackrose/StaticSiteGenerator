import unittest

from textnode import TextType, TextNode
from nodeparsing import split_nodes_image, split_nodes_link

class TestNodeExtractLinkImage(unittest.TestCase):
    def test_image(self):
        node = TextNode("This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png) in the node", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        total = len(new_nodes)
        self.assertEqual(total, 3)

    def test_link(self):
        node = TextNode("This is a text with a [link](http://www.google.com) in the node", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        total = len(new_nodes)
        self.assertEqual(total, 3)

    def test_image_multiple(self):
        node = TextNode("This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png) in the node and another ![image](https://i.imgur.com/zjjcJKZ.png) in the node", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        total = len(new_nodes)
        self.assertEqual(total, 5)

    def test_link_multiple(self):
        node = TextNode("This is a text with a [link](http://www.google.com) in the node and another [link](http://www.google.com) in the node", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        total = len(new_nodes)
        self.assertEqual(total, 5)

    def test_link_and_image(self):
        node = TextNode("This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](http://www.google.com) in the node", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        new_nodes_link = split_nodes_link(new_nodes)
        total = len(new_nodes_link)
        self.assertEqual(total, 5)

    def test_no_image(self):
        node = TextNode("This is a text with only text nodes in the node", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        total = len(new_nodes)
        self.assertEqual(total, 1)

    def test_no_link(self):
        node = TextNode("This is a text with only text nodes in the node", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        total = len(new_nodes)
        self.assertEqual(total, 1)   


if __name__ == "__main__":
    unittest.main()