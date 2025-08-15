from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text (plain)"
    BOLD =  "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "Links, in this format: [anchor text](url)"
    IMAGE = "Images, in this format: ![alt text](url)"


class TextNode():
    def __init__(self, text, text_type:TextType, url=None):
        self.text = text
        # text_type is the enum TextType
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node:TextNode):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            params = { "href" : text_node.url}
            return LeafNode("a", text_node.text, params)
        case TextType.IMAGE:
            params = { "src" : text_node.url,
                        "alt" : text_node.text,
                    }
            return LeafNode("img", text_node.text, params)
        case _:
            raise TypeError("Error: Invalid text type provided")

