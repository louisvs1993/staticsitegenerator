from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
            super().__init__(tag, None, children, props)
    
    def to_html(self):
          if self.tag == None:
                raise ValueError
          elif self.children == None:
                raise ValueError("No children were given")
          else:
                childrenString = ""
                for child in self.children:
                      childrenString = childrenString + child.to_html()
                htmlString = f"<{self.tag}{self.props_to_html()}>{childrenString}</{self.tag}>"
                return htmlString