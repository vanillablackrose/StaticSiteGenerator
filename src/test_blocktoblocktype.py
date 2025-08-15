import unittest

from blockparsing import block_to_block_type, BlockType

# these tests have all unnecessary new lines stripped out as the conversion method assumes that the block content passed to it has been stripped
# and will fail and create a paragraph if the content is not stripped
class TestBlockToBlockType(unittest.TestCase):
    def test_heading_1(self):
        markdown = """# Heading 1 code here
This is the same heading"""
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.HEADING)

    def test_heading_2(self):
        markdown = """## Heading 2 code here
This is the same heading"""
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.HEADING)

    def test_heading_3(self):
        markdown = """### Heading 3 code here
This is the same heading"""
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.HEADING)
    
    def test_heading_4(self):
        markdown = """#### Heading 4 code here
This is the same heading"""
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.HEADING)

    def test_heading_5(self):
        markdown = """##### Heading 1 code here
This is the same heading"""
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.HEADING)

    def test_heading_6(self):
        markdown = """###### Heading 1 code here
This is the same heading"""
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.HEADING)

    def test_code(self):
        markdown = """``` code block starts here
This is the same code block ```"""
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.CODE)

    def test_blockquote(self):
        markdown = """> Quote line 1
> Quote line 2"""
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.QUOTE)


    def test_unordered_list(self):
        markdown = """- list item one
- list item two
- list item three"""
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        markdown = """1. list item one
2. list item two
3. list item three"""
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.ORDERED_LIST)

    def test_paragraph(self):
        markdown = """This is an example paragraph.
It has multiple lines."""
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.PARAGRAPH)

    def test_invalid_heading(self):
        markdown = """#This heading lacks the space after the #"""
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.PARAGRAPH)

    def test_invalid_code(self):
        markdown = """``` This code block lacks the closing quotes
This is the same code block """
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.PARAGRAPH)

    def test_invalid_blockquote(self):
        markdown = """> Quote line 1
 Quote line 2 lacks the >"""
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.PARAGRAPH)

    def test_invalid_unordered_list(self):
        markdown = """- list item one
 list item two lacks a dash
- list item three"""
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.PARAGRAPH)

    def test_invalid_ordered_list(self):
        markdown = """1. list item one
2. list item two
4. list item three skipped the number 3"""
        type = block_to_block_type(markdown)
        self.assertEqual(type, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()