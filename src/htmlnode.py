class HTMLNode():

    def __init__(self, tag=None, value=None, children:list=None, props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Error: This method is not implemented at the base level.")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        html_string = " "        

        for key in self.props:
            html_string += f"{key}='{self.props[key]}' "

        return html_string
    
    def __repr__(self):
        node_string = ""
        if self.tag != None:            
            node_string = f"<{self.tag}"        
            node_string += self.props_to_html() + ">"
        elif self.props != None:
            node_string += self.props_to_html()

        if self.value != None:
            node_string += self.value

        if self.children != None:
            for child in self.children:
                node_string += repr(child)
        
        if self.tag != None: 
            node_string += f"</{self.tag}>"

        return node_string


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Error: The Leaf node does not have a value and this is required")
        
        if self.tag == None:
            return self.value
        else:
            node_string = f"<{self.tag}"        
            node_string += self.props_to_html() + ">"
            node_string += self.value
            node_string += f"</{self.tag}>"

            return node_string
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag == None:
            raise ValueError("Error: The Parent node does not have a tag and this is required")
        
        if self.children == None:
            raise ValueError("Error: The Parent node does not have children and this is required")
        
        node_string = f"<{self.tag}"        
        node_string += self.props_to_html() + ">"
        for child in self.children:
            node_string += child.to_html()

        node_string += f"</{self.tag}>"

        return node_string
    
    def add_children(self, children):
        self.children = children

    def add_child(self, child):
        if self.children == None:
            self.children = [child]
        else:
            self.children.extend(child)
    
    
            
