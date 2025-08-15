import unittest

from markdowntohtml import markdown_to_html_node, HTMLNode

# these tests have all unnecessary new lines stripped out as the conversion method assumes that the block content passed to it has been stripped
# and will fail and create a paragraph if the content is not stripped
class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        test_str = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"

        self.assertEqual(html, test_str)

    def test_heading_1(self):
        markdown = """# Heading 1 code here
This is the same heading with some **bold text** thrown in for good measure"""
        
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        test_str = "<div><h1>Heading 1 code here This is the same heading with some <b>bold text</b> thrown in for good measure</h1></div>"
        self.assertEqual(html, test_str)

    def test_heading_2(self):
        markdown = """## Heading 2 code here
This is the same heading with some **bold text** thrown in for good measure"""

        node = markdown_to_html_node(markdown)
        html = node.to_html()
        test_str = "<div><h2>Heading 2 code here This is the same heading with some <b>bold text</b> thrown in for good measure</h2></div>"
        self.assertEqual(html, test_str)

    def test_heading_3(self):
        markdown = """### Heading 3 code here
This is the same heading with some **bold text** thrown in for good measure"""

        node = markdown_to_html_node(markdown)
        html = node.to_html()
        test_str = "<div><h3>Heading 3 code here This is the same heading with some <b>bold text</b> thrown in for good measure</h3></div>"
        self.assertEqual(html, test_str)
    
    def test_heading_4(self):
        markdown = """#### Heading 4 code here
This is the same heading with some **bold text** thrown in for good measure"""

        node = markdown_to_html_node(markdown)
        html = node.to_html()
        test_str = "<div><h4>Heading 4 code here This is the same heading with some <b>bold text</b> thrown in for good measure</h4></div>"
        self.assertEqual(html, test_str)

    def test_heading_5(self):
        markdown = """##### Heading 5 code here
This is the same heading with some **bold text** thrown in for good measure"""

        node = markdown_to_html_node(markdown)
        html = node.to_html()
        test_str = "<div><h5>Heading 5 code here This is the same heading with some <b>bold text</b> thrown in for good measure</h5></div>"
        self.assertEqual(html, test_str)

    def test_heading_6(self):
        markdown = """###### Heading 6 code here
This is the same heading with some **bold text** thrown in for good measure"""

        node = markdown_to_html_node(markdown)
        html = node.to_html()
        test_str = "<div><h6>Heading 6 code here This is the same heading with some <b>bold text</b> thrown in for good measure</h6></div>"
        self.assertEqual(html, test_str)

    def test_blockquote(self):
        markdown = """> Quote line 1
> Quote line 2
> Quote line 2 _italic text here_
> Quote **bolded line** inserted
"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        test_str = "<div><blockquote>Quote line 1 Quote line 2 Quote line 2 <i>italic text here</i> Quote <b>bolded line</b> inserted</blockquote></div>"

        self.assertEqual(html, test_str)

    def test_unordered_list(self):
        markdown = """- list item `code block` one
- list item _italic text_ two
- list item three"""
        
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        test_str = "<div><ul><li>list item <code>code block</code> one</li><li>list item <i>italic text</i> two</li><li>list item three</li></ul></div>"
        self.assertEqual(html, test_str)

    def test_ordered_list(self):
        markdown = """1. list item **bold here** one
2. list item two
3. list item _italic here_ three"""
        
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        test_str = "<div><ol><li>list item <b>bold here</b> one</li><li>list item two</li><li>list item <i>italic here</i> three</li></ol></div>"
        self.assertEqual(html, test_str)


    def test_heading_paragraph_and_list(self):
        markdown = """# Heading 1 code here
This is the same heading with some **bold text** thrown in for good measure

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

1. list item **bold here** one
2. list item two
3. list item _italic here_ three
"""   
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        test_str = "<div><h1>Heading 1 code here This is the same heading with some <b>bold text</b> thrown in for good measure</h1><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p><ol><li>list item <b>bold here</b> one</li><li>list item two</li><li>list item <i>italic here</i> three</li></ol></div>"
        self.assertEqual(html, test_str)


if __name__ == "__main__":
    unittest.main()
