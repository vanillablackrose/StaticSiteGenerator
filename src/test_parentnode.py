import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_tag_error_case(self):
        parent_node = ParentNode(None, [])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_children_error_case(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError, parent_node.to_html)

    def test_with_props(self):
        props = { 
            "src" : "http://www.google.com", 
            "target" : "_blank",
        }
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props)
        self.assertEqual(parent_node.to_html(), "<div src='http://www.google.com' target='_blank' ><span>child</span></div>")

    def test_with_multiple_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><span>child2</span></div>")

    def test_with_child_props(self):
        props = { 
            "src" : "http://www.google.com", 
            "target" : "_blank",
        }
        child_node = LeafNode("span", "child", props)
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span src='http://www.google.com' target='_blank' >child</span></div>")

    def test_with_parent_and_child_props(self):
        props = { 
            "src" : "http://www.google.com", 
            "target" : "_blank",
        }
        child_props = { 
            "src" : "http://www.yahoo.com", 
            "target" : "_blank",
        }
        child_node = LeafNode("span", "child", child_props)
        parent_node = ParentNode("div", [child_node], props)
        self.assertEqual(parent_node.to_html(), "<div src='http://www.google.com' target='_blank' ><span src='http://www.yahoo.com' target='_blank' >child</span></div>")


if __name__ == "__main__":
    unittest.main()