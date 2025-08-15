import unittest

from nodeparsing import text_to_textnodes

class TestNodeTextToTextNodes(unittest.TestCase):
    def test_text(self):
        text = "This is a text with only text nodes in the node"
        new_nodes = text_to_textnodes(text)
        total = len(new_nodes)
        self.assertEqual(total, 1)

    def test_bold(self):
        text = "This is a text with **a bold node here** in the node"
        new_nodes = text_to_textnodes(text)
        total = len(new_nodes)
        self.assertEqual(total, 3)

    def test_italic(self):
        text = "This is a text with _an italic node here_ in the node"
        new_nodes = text_to_textnodes(text)
        total = len(new_nodes)
        self.assertEqual(total, 3)

    def test_code(self):
        text = "This is a text with `a code node here` in the node"
        new_nodes = text_to_textnodes(text)
        total = len(new_nodes)
        self.assertEqual(total, 3)

    def test_bold_and_italic(self):
        text = "This is a text with **a bold node here** _and italic node here_ in the node"
        new_nodes = text_to_textnodes(text)
        total = len(new_nodes)
        self.assertEqual(total, 5)

    def test_bold_and_italic_and_code(self):
        text = "This is a text with **a bold node here** _and italic node here_ and a `a code node here` in the node"
        new_nodes = text_to_textnodes(text)
        total = len(new_nodes)
        self.assertEqual(total, 7)

    def test_image(self):
        text = "This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png) in the node"
        new_nodes = text_to_textnodes(text)
        total = len(new_nodes)
        self.assertEqual(total, 3)

    def test_link(self):
        text = "This is a text with a [link](http://www.google.com) in the node"
        new_nodes = text_to_textnodes(text)
        total = len(new_nodes)
        self.assertEqual(total, 3)

    def test_image_multiple(self):
        text = "This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png) in the node and another ![image](https://i.imgur.com/zjjcJKZ.png) in the node"
        new_nodes = text_to_textnodes(text)
        total = len(new_nodes)
        self.assertEqual(total, 5)

    def test_link_multiple(self):
        text = "This is a text with a [link](http://www.google.com) in the node and another [link](http://www.google.com) in the node"
        new_nodes = text_to_textnodes(text)
        total = len(new_nodes)
        self.assertEqual(total, 5)

    def test_link_and_image(self):
        text = "This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](http://www.google.com) in the node"
        new_nodes = text_to_textnodes(text)
        total = len(new_nodes)
        self.assertEqual(total, 5)

    def test_bold_and_italic_and_code_and_img_and_link(self):
        text = "This is a text with **a bold node here** _and italic node here_ and a `a code node here` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](http://www.google.com) in the node"
        new_nodes = text_to_textnodes(text)
        total = len(new_nodes)
        self.assertEqual(total, 11)



if __name__ == "__main__":
    unittest.main()