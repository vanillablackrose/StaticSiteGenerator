
from blockparsing import BlockType, markdown_to_blocks, block_to_block_type
from textnode import TextNode, TextType, text_node_to_html_node
from nodeparsing import text_to_textnodes
from htmlnode import HTMLNode, ParentNode, LeafNode

def markdown_to_html_node(markdown):
    markdown = markdown.strip()
    blocks = markdown_to_blocks(markdown)

    html_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        new_child = block_to_htmlnode(block, block_type)
        html_nodes.append(new_child)
 
    html_parent = ParentNode("div", html_nodes)

    return html_parent

def block_to_htmlnode(block, block_type:BlockType):
    match block_type:
        case BlockType.HEADING:
            return block_to_heading(block)
        
        case BlockType.QUOTE:
            return block_to_quote(block)
        
        case BlockType.UNORDERED_LIST:
            return block_to_unordered_list(block)

        case BlockType.ORDERED_LIST:
            return block_to_ordered_list(block)

        case BlockType.CODE:
            return block_to_code(block)

        case BlockType.PARAGRAPH:
            return block_to_paragraph(block)

        
def text_to_children(block, block_type:BlockType):
    child_text = []
    if block_type == BlockType.UNORDERED_LIST or block_type == BlockType.ORDERED_LIST:
        lines = block.split("\n")

        children = []
        for line in lines:
            line = line.strip()

            ## remove the following prefixes:
            #. - >
            if block_type == BlockType.UNORDERED_LIST:
                line = line.removeprefix("- ")
            else:
                line = line[3:]

            curr_children = []
            text_nodes = text_to_textnodes(line)
            for child_node in text_nodes:
                child_html = text_node_to_html_node(child_node)
                curr_children.append(child_html)
            ##create one master leaf node to represent this list item row. this is what is added to the children list
            list_node = ParentNode("li", curr_children)
            children.append(list_node)

        return children    
    elif block_type == BlockType.QUOTE:
        lines = block.split("\n")

        text = ""
        for line in lines:
            line = line.strip()
            line = line.removeprefix(">")
            text += line

        text = text.strip()
        child_text.extend(text_to_textnodes(text))
    else:
        text = block.replace("\n", " ")
        child_text.extend(text_to_textnodes(text))

    children = []

    for child_node in child_text:
        child_html = text_node_to_html_node(child_node)
        children.append(child_html)

    return children

def block_to_heading(block):
    heading_count = block.count("#", 0, 7)
    
    while block.startswith("#"):
        block = block.removeprefix("#")

    block = block.lstrip()
    
    children = text_to_children(block, BlockType.HEADING)

    heading_node = ParentNode(f"h{heading_count}", children)
    return heading_node

def block_to_quote(block):
    children = text_to_children(block, BlockType.QUOTE)

    quote_node = ParentNode("blockquote", children)
    return quote_node

def block_to_code(block):
    line = block[3:-3]
    line = line.lstrip()
 
    code_node = LeafNode("code", line)
    pre_node = ParentNode("pre", [code_node])
    return pre_node

def block_to_unordered_list(block):
    children = text_to_children(block, BlockType.UNORDERED_LIST)

    unordered_node = ParentNode("ul", children)
    return unordered_node

def block_to_ordered_list(block):
    children = text_to_children(block, BlockType.ORDERED_LIST)

    ordered_node = ParentNode("ol", children)
    return ordered_node

def block_to_paragraph(block):
    children = text_to_children(block, BlockType.PARAGRAPH)

    paragraph_node = ParentNode("p", children)
    return paragraph_node