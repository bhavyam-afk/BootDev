import unittest
from htmlnode import HTMLNode


class TestHTMLNodePropsToHTML(unittest.TestCase):

    def test_props_to_html_basic(self):
        node = HTMLNode(
            tag="a",
            props={
                "href": "https://www.google.com",
                "target": "_blank"
            }
        )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty_dict(self):
        node = HTMLNode(tag="p", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none(self):
        node = HTMLNode(tag="div", props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_single_prop(self):
        node = HTMLNode(tag="img", props={"src": "image.png"})
        self.assertEqual(node.props_to_html(), ' src="image.png"')


if __name__ == "__main__":
    unittest.main()
