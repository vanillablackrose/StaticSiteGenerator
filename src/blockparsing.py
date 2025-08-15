from enum import Enum
from textnode import TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph <p>"
    HEADING =  "heading <h1-6>"
    CODE = "Code <code>"
    QUOTE = "Quote <blockquote>"
    UNORDERED_LIST = "Unordered List <ul>"
    ORDERED_LIST = "Ordered List <ol>"

def markdown_to_blocks(markdown):
    # split on line breaks
    # discard empty content
    # create text nodes of everything else
    blocks = []

    md_lines = markdown.split("\n\n")

    for line in md_lines:
        # trim down the content
        # skip if empty

        line = line.strip()
        if line != "":
            blocks.append(line)

    return blocks

def block_to_block_type(block):
    ## check if a heading
    if block_is_heading(block):
        return BlockType.HEADING
    elif block_is_code(block):
        return BlockType.CODE
    elif block_is_quote(block):
        return BlockType.QUOTE
    elif block_is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    elif block_is_ordered_list(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def block_is_heading(block):
    prefixes = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    return block.startswith(prefixes)
    
def block_is_code(block):
    ## check if first line starts with ``` and last line ends with ```
    lines = block.split("\n")
    first = lines[0]
    last = lines[-1]

    return first.startswith("```") and last.endswith("```")

def block_is_quote(block):
    # every line MUST start with >
    lines = block.split("\n")

    for line in lines:
        if not line.startswith(">"):
            return False
        
    return True

def block_is_unordered_list(block):
    # every line MUST start with - followed by a space
    lines = block.split("\n")

    for line in lines:
        if not line.startswith("- "):
            return False
        
    return True

def block_is_ordered_list(block):
    # every line MUST start with number. space and the numbers MUST be in order
    lines = block.split("\n")
    curr_num = 1

    for line in lines:
        if not line.startswith(f"{curr_num}. "):
            return False
        curr_num += 1
        
    return True
