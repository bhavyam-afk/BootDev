from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    QUOTE = "quote"
    CODE = "code"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")

    blocks = []
    for block in raw_blocks:
        stripped = block.strip()
        if stripped != "":
            blocks.append(stripped)

    return blocks


def block_to_block_type(block):
    lines = block.split("\n")

    # 1. Heading
    if block.startswith("#"):
        count = 0
        for ch in block:
            if ch == "#":
                count += 1
            else:
                break
        if 1 <= count <= 6 and len(block) > count and block[count] == " ":
            return BlockType.HEADING

    # 2. Code block
    if (
        len(lines) >= 2
        and lines[0] == "```"
        and lines[-1] == "```"
    ):
        return BlockType.CODE

    # 3. Quote block
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # 4. Unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # 5. Ordered list
    expected = 1
    ordered = True
    for line in lines:
        prefix = f"{expected}. "
        if not line.startswith(prefix):
            ordered = False
            break
        expected += 1
    if ordered:
        return BlockType.ORDERED_LIST

    # 6. Paragraph
    return BlockType.PARAGRAPH

