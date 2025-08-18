class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
            self.value = value
            self.tag = tag
            self.children = children
            self.props = props
        
    def __eq__(self, other):
        if self.value == other.value and self.tag == other.tag and self.children == other.children and self.props == other.props:
            return True
        else:
            return False
    
    def to_html(self):
        raise NotImplementedError("Override in childclass")
    
    def props_to_html(self):
        if self.props != None:
            prop_string = ""
            for key, value in self.props.items():
                prop_string = prop_string + f" {key}=\"{value}\""
            return prop_string
        else:
            return ""
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
            
    

