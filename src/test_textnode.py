import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.__repr__(), "TextNode(This is a text node, TextType.BOLD, None)")

    def test_text_type_notequal(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_notequal(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node but different", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_url_defaults_to_none(self):
        node = TextNode("some text", TextType.TEXT)
        self.assertIsNone(node.url)
    
    def test_url_difference(self):
        node1 = TextNode("text", TextType.TEXT, url=None)
        node2 = TextNode("text", TextType.TEXT, url="http://example.com")
        self.assertNotEqual(node1, node2)

    def test_image(self):
        node = TextNode("A bear", TextType.IMAGE, "https://boot.dev/bear.png")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "https://boot.dev/bear.png")
        self.assertEqual(html_node.props["alt"], "A bear")
    
    def test_link(self):
        node = TextNode("A bear", TextType.LINK, "https://boot.dev/bear.png")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "A bear")
        self.assertEqual(html_node.props["href"], "https://boot.dev/bear.png")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
        


if __name__ == "__main__":
    unittest.main()