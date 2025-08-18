import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_tagless(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_leaf_to_html_prop(self):
        node = LeafNode("p", "Hello, world!", {"style":"text-align:right", "id":"plaintext"})
        self.assertEqual(node.to_html(), "<p style=\"text-align:right\" id=\"plaintext\">Hello, world!</p>")
    
    def test_leaf_to_html_no_value_raises_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()