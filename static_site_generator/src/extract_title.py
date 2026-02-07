def extract_title(markdown: str) -> str:
    for line in markdown.split("\n"):
        line = line.strip()
        if line.startswith("# ") and not line.startswith("##"):
            return line[2:].strip()

    raise Exception("No h1 header found in markdown")
