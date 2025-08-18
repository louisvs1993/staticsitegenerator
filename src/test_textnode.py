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

    def test_text_type(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
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
        


if __name__ == "__main__":
    unittest.main()