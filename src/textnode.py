from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(self):
    if self.text_type not in TextType:
        raise Exception("Type not correct")
    elif self.text_type == TextType.TEXT:
        return LeafNode(None, self.text)
    elif self.text_type == TextType.BOLD:
        return LeafNode("b", self.text)
    elif self.text_type == TextType.ITALIC:
        return LeafNode("i", self.text)
    elif self.text_type == TextType.CODE:
        return LeafNode("code", self.text)
    elif self.text_type == TextType.LINK:
        if self.url != None:
            return LeafNode("a", self.text, {"href":self.url})
        else:
            raise Exception("Url required")
    elif self.text_type == TextType.IMAGE:
        if self.url != None:
            return LeafNode("img", "", {"src":self.url,"alt":self.text})
        else:
            raise Exception("Url required")