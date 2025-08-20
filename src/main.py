import sys
from generatehtmlfile import copy_static, generate_pages_recursive
WORKING_DIR = "."


def main():
    basepath = sys.argv[1]
    if basepath == "":
        basepath = "/"

    copy_static(WORKING_DIR) 

    from_path = WORKING_DIR + "/content"
    template_path = "template.html"
    dest_path = WORKING_DIR + "/docs"

    generate_pages_recursive(from_path, template_path, dest_path, basepath)





main()