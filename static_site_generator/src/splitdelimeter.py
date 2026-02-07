from textnode import TextNode, TextType
from markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception(f"Invalid Markdown syntax: unclosed '{delimiter}'")

        for i, part in enumerate(parts):
            if part == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(node)
            continue

        remaining = text

        for alt, url in images:
            markdown = f"![{alt}]({url})"
            before, _, after = remaining.partition(markdown)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            remaining = after

        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))

    return new_nodes




def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(node)
            continue

        remaining = text

        for label, url in links:
            markdown = f"[{label}]({url})"
            before, _, after = remaining.partition(markdown)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(label, TextType.URL, url))
            remaining = after

        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))

    return new_nodes




