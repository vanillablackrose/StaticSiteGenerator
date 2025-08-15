from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type:TextType):
    new_nodes = []

    for node in old_nodes:
        text = node.text  
        parent_type = node.text_type      
        new_nodes.extend(split_text_delimiter(text, parent_type, delimiter, text_type))

    return new_nodes

def split_text_delimiter(text, parent_type:TextType, delimiter, text_type:TextType):
    new_nodes = []
    curr_text = None
    curr_type = None
    remainder = text

    while remainder != "":        
        if curr_type != None:
            # do one split. the first string will be up to the second found delimiter.
            # the second will be the remainder of the string
            # IF the second is empty, throw a value error
            # else create a type node and set the type node string to None
            text_list = remainder.split(delimiter, 1)
            total = len(text_list)
            if total == 1:
                raise ValueError(f"Error: The text {text} contains mismatched delmiiters when parsing the delimiter {delimiter}")
            else:
                curr_type = text_list[0]
                if total > 1:
                    remainder = text_list[1]
                else:
                    remainder = ""

                if curr_text != "":
                    new_nodes.append(TextNode(curr_type, text_type))
                curr_type = None

        elif curr_text == None:
            # do one split. the first string will be up to the first found delimiter.
            # the second will be the remainder of the string
            # then create a text node and set the type node string to None
            text_list = remainder.split(delimiter, 1)
            curr_text = text_list[0]
            total = len(text_list)
            if total > 1:
                remainder = text_list[1]
            else:
                remainder = ""

            curr_type = ""

            if curr_text != "":
                new_nodes.append(TextNode(curr_text, parent_type))
            curr_text = None

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)            

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        text = node.text  
        parent_type = node.text_type 
        ## extract the image tuples
        images = extract_markdown_images(text) 
        if len(images) != 0:    
            new_nodes.extend(split_text_tuples(text, parent_type, images, TextType.IMAGE))
        else:
            ## if there are no images in the node, just preserve the original
            new_nodes.append(node)

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        text = node.text  
        parent_type = node.text_type 
        ## extract the image tuples
        links = extract_markdown_links(text) 
        if len(links) != 0:    
            new_nodes.extend(split_text_tuples(text, parent_type, links, TextType.LINK))
        else:
            ## if there are no images in the node, just preserve the original
            new_nodes.append(node)

    return new_nodes

def split_text_tuples(text, parent_type:TextType, matches, tuple_type:TextType):
    new_nodes = []
    remainder = text    

    for match in matches:
        #split up to the tuple values
        #create a text node for the part before
        #create the image/link node
        #set the remainder

        match_text = match[0]
        url = match[1]
        match_str = ""

        # split on the image/link
        if tuple_type == TextType.IMAGE:
            match_str = f"![{match_text}]({url})"
        elif tuple_type == TextType.LINK:
            match_str = f"[{match_text}]({url})"
        else:
            TypeError("Error: Invalid text type provided")

        text_list = remainder.split(match_str, 1)

        # set the remainder
        curr_text = text_list[0]
        total = len(text_list)
        if total > 1:
            remainder = text_list[1]
        else:
            remainder = ""

        # create the prior node
        if curr_text != "":
            new_nodes.append(TextNode(curr_text, parent_type))

        # create the image/link
        new_nodes.append(TextNode(match_text, parent_type, url))

    #handle the remainder
    if remainder != "":
        new_nodes.append(TextNode(remainder, parent_type))

    return new_nodes

def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.TEXT)]
    
    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)

    return text_nodes