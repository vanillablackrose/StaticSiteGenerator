import unittest

from generatehtmlfile import extract_title

# these tests have all unnecessary new lines stripped out as the conversion method assumes that the block content passed to it has been stripped
# and will fail and create a paragraph if the content is not stripped
class TestMarkdownToHTML(unittest.TestCase):

    def test_heading_1(self):
        markdown = """# Heading 1 code here
This is the same heading with some **bold text** thrown in for good measure

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        
        title = extract_title(markdown)
        test_str = "Heading 1 code here\nThis is the same heading with some **bold text** thrown in for good measure"
        self.assertEqual(title, test_str)

    def test_no_heading(self):
        markdown = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        self.assertRaises(ValueError, extract_title, markdown)




if __name__ == "__main__":
    unittest.main()