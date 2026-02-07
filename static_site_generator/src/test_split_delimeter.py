import unittest
from textnode import TextNode, TextType
from splitdelimeter import split_nodes_delimiter


def test_basic_bold():
    nodes = [TextNode("Hello **world**", TextType.TEXT)]
    result = split_nodes_delimiter(nodes, "**", TextType.BOLD)

    assert result == [
        TextNode("Hello ", TextType.TEXT),
        TextNode("world", TextType.BOLD),
    ]


def test_multiple_bold():
    nodes = [TextNode("a **b** c **d**", TextType.TEXT)]
    result = split_nodes_delimiter(nodes, "**", TextType.BOLD)

    assert result == [
        TextNode("a ", TextType.TEXT),
        TextNode("b", TextType.BOLD),
        TextNode(" c ", TextType.TEXT),
        TextNode("d", TextType.BOLD),
    ]


def test_italic():
    nodes = [TextNode("this *works*", TextType.TEXT)]
    result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)

    assert result == [
        TextNode("this ", TextType.TEXT),
        TextNode("works", TextType.ITALIC),
    ]


def test_code():
    nodes = [TextNode("use `code` here", TextType.TEXT)]
    result = split_nodes_delimiter(nodes, "`", TextType.CODE)

    assert result == [
        TextNode("use ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode(" here", TextType.TEXT),
    ]


def test_non_text_node_unchanged():
    nodes = [TextNode("bold", TextType.BOLD)]
    result = split_nodes_delimiter(nodes, "**", TextType.BOLD)

    assert result == nodes


if __name__ == "__main__":
    unittest.main()
