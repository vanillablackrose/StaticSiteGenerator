from enum import Enum

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