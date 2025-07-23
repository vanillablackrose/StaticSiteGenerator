

class HTMLNode():

    def __init__(self, tag=None, value=None, children:list=None, props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception(NotImplementedError)
    
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


