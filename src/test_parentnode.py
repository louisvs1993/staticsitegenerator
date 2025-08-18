import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_to_html_div(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")])
        self.assertEqual(node.to_html(), "<div><p>Hello, world!</p></div>")
    
    def test_parent_to_html_body(self):
        node = ParentNode("body", [ParentNode("div", [LeafNode("p", "Hello, world!")])])
        self.assertEqual(node.to_html(), "<body><div><p>Hello, world!</p></div></body>")

    def test_parent_to_html_no_tag_raises_error(self):
        node = ParentNode(None, [LeafNode("p", "Hello, world!")])
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_parent_to_html_no_children_raises_error(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()