import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "Plain text")
        node2 = HTMLNode("p", "Plain text")
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = HTMLNode("p", "Plain text")
        self.assertEqual(node.__repr__(), "HTMLNode(p, Plain text, None, None)")

    def test_props_to_html(self):
        node = HTMLNode("p", "Plain text", None, {"style":"text-align:right", "id":"plaintext"})
        self.assertEqual(node.props_to_html()," style=\"text-align:right\" id=\"plaintext\"")


if __name__ == "__main__":
    unittest.main()