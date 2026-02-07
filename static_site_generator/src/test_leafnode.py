import unittest
from leafnode import LeafNode


def test_leafnode_no_tag_returns_value_only():
    node = LeafNode(tag=None, value="Hello World")
    assert node.to_html() == "Hello World"


def test_leafnode_paragraph():
    node = LeafNode(tag="p", value="This is a paragraph")
    assert node.to_html() == "<p>This is a paragraph</p>"


def test_leafnode_with_props():
    props = {
        "href": "https://www.google.com",
        "target": "_blank"
    }
    node = LeafNode(tag="a", value="Google", props=props)
    assert node.to_html() == '<a href="https://www.google.com" target="_blank">Google</a>'


def test_leafnode_bold():
    node = LeafNode(tag="b", value="Important")
    assert node.to_html() == "<b>Important</b>"


def test_leafnode_repr():
    node = LeafNode(tag="p", value="Hello", props={"class": "text"})
    assert repr(node) == "LeafNode(p, Hello, {'class': 'text'})"


def test_leafnode_no_children_allowed():
    node = LeafNode(tag="p", value="Test")
    assert node.children is None


if __name__ == "__main__":
    unittest.main()