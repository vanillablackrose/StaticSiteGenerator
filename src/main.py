from textnode import TextNode
from textnode import TextType

def main():

    node = TextNode("This is some sample text", TextType.LINK, "http://www.google.com")

    print(node)    


main()