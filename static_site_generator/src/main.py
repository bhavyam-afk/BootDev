from generate_pages_recursive import generate_pages_recursive
from copy_static_to_public import copy_recursive

def main():
    copy_recursive("static", "public")

    generate_pages_recursive(
        "content",
        "template.html",
        "public"
    )

if __name__ == "__main__":
    main()
