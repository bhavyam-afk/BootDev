import os
from generate_page import generate_page  # or wherever it lives

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Ensure destination directory exists
    os.makedirs(dest_dir_path, exist_ok=True)

    for entry in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        # 📁 If it's a directory → recurse
        if os.path.isdir(content_path):
            generate_pages_recursive(
                content_path,
                template_path,
                dest_path
            )

        # 📄 If it's a markdown file → generate HTML
        elif entry.endswith(".md"):
            output_html = dest_path.replace(".md", ".html")

            print(
                f"Generating page from {content_path} "
                f"to {output_html} using {template_path}"
            )

            generate_page(
                content_path,
                template_path,
                output_html
            )
