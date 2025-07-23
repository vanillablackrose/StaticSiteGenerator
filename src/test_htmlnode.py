import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_node(self):
        node = HTMLNode()
        expected_value = ""
        actual_value = f'{node}'
        self.assertEqual(expected_value, actual_value)

    def test_simple_node(self):
        node = HTMLNode("a")
        expected_value = "<a></a>"
        actual_value = f'{node}'
        self.assertEqual(expected_value, actual_value)
    
    def test_text_node(self):
        node = HTMLNode(None, "Here is some text")
        expected_value = "Here is some text"
        actual_value = f'{node}'
        self.assertEqual(expected_value, actual_value)

    def test_node_with_text(self):
        node = HTMLNode("div", "Here is some text")
        expected_value = "<div>Here is some text</div>"
        actual_value = f'{node}'
        self.assertEqual(expected_value, actual_value)

    def test_properties(self):
        props = { 
            "src" : "http://www.google.com", 
            "target" : "_blank",
        }

        node = HTMLNode(None, None, None, props)
        expected_value = " src='http://www.google.com' target='_blank' "
        actual_value = f'{node}'
        self.assertEqual(expected_value, actual_value)

    def test_node_with_children(self):
        child1 = HTMLNode("span", "Sample Text")
        child2 = HTMLNode("span", "Sample Text 2")

        children = [child1, child2]

        node = HTMLNode("div", None, children)
        expected_value = "<div><span>Sample Text</span><span>Sample Text 2</span></div>"
        actual_value = f'{node}'
        self.assertEqual(expected_value, actual_value)

    def test_node_with_children_and_props(self):
        child1 = HTMLNode("span", "Sample Text")
        child2 = HTMLNode("span", "Sample Text 2")

        children = [child1, child2]

        props = { 
            "src" : "http://www.google.com", 
            "target" : "_blank",
        }

        node = HTMLNode("div", None, children, props)
        expected_value = "<div src='http://www.google.com' target='_blank' ><span>Sample Text</span><span>Sample Text 2</span></div>"
        actual_value = f'{node}'
        self.assertEqual(expected_value, actual_value)

    def test_node_with_text_and_children_and_props(self):
        child1 = HTMLNode("span", "Sample Text")
        child2 = HTMLNode("span", "Sample Text 2")

        children = [child1, child2]

        props = { 
            "src" : "http://www.google.com", 
            "target" : "_blank",
        }

        node = HTMLNode("div", "Here is some text", children, props)
        expected_value = "<div src='http://www.google.com' target='_blank' >Here is some text<span>Sample Text</span><span>Sample Text 2</span></div>"
        actual_value = f'{node}'
        self.assertEqual(expected_value, actual_value)




if __name__ == "__main__":
    unittest.main()