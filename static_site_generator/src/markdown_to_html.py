from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from blocks import BlockType, markdown_to_blocks, block_to_block_type
from text_to_node import text_to_textnodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = []

    for block in blocks:
        block_type = block_to_block_type(block)

        # HEADING
        if block_type == BlockType.HEADING:
            level = len(block.split(" ")[0])
            text = block[level + 1:]

            text_nodes = text_to_textnodes(text)
            html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]

            html_blocks.append(
                ParentNode(f"h{level}", html_nodes, None)
            )

        # PARAGRAPH
        elif block_type == BlockType.PARAGRAPH:
            text_nodes = text_to_textnodes(block)
            html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]

            html_blocks.append(
                ParentNode("p", html_nodes, None)
            )

        # QUOTE
        elif block_type == BlockType.QUOTE:
            lines = [line.lstrip("> ").rstrip() for line in block.split("\n")]
            text = " ".join(lines)

            text_nodes = text_to_textnodes(text)
            html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]

            html_blocks.append(
                ParentNode("blockquote", html_nodes, None)
            )

        # UNORDERED LIST
        elif block_type == BlockType.UNORDERED_LIST:
            items = block.split("\n")
            li_nodes = []

            for item in items:
                text = item[2:]
                text_nodes = text_to_textnodes(text)
                html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]

                li_nodes.append(
                    ParentNode("li", html_nodes, None)
                )

            html_blocks.append(
                ParentNode("ul", li_nodes, None)
            )

        # ORDERED LIST
        elif block_type == BlockType.ORDERED_LIST:
            items = block.split("\n")
            li_nodes = []

            for item in items:
                text = item.split(". ", 1)[1]
                text_nodes = text_to_textnodes(text)
                html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]

                li_nodes.append(
                    ParentNode("li", html_nodes, None)
                )

            html_blocks.append(
                ParentNode("ol", li_nodes, None)
            )

        # CODE BLOCK (NO inline parsing)
        elif block_type == BlockType.CODE:
            code_text = "\n".join(block.split("\n")[1:-1])

            text_node = TextNode(code_text, TextType.TEXT)
            code_html = text_node_to_html_node(text_node)

            html_blocks.append(
                ParentNode("pre", [
                    ParentNode("code", [code_html], None)
                ], None)
            )

    return ParentNode("div", html_blocks, None)
