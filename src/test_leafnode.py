import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, world!")
        self.assertEqual(node.to_html(), "<div>Hello, world!</div>")

    def test_leaf_to_html_link(self):
        props = { 
            "src" : "http://www.google.com", 
            "target" : "_blank",
        }
        node = LeafNode("a", "Link to google", props)
        self.assertEqual(node.to_html(), "<a src='http://www.google.com' target='_blank' >Link to google</a>")

    def test_text_only_node(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_error_condition(self):
        node = LeafNode(None, None)
        self.assertRaises(ValueError, node.to_html)

if __name__ == "__main__":
    unittest.main()