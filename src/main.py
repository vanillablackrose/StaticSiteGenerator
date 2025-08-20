from generatehtmlfile import copy_static, generate_pages_recursive
WORKING_DIR = "."


def main():
    copy_static(WORKING_DIR) 

    from_path = WORKING_DIR + "/content"
    template_path = "template.html"
    dest_path = WORKING_DIR + "/public"

    generate_pages_recursive(from_path, template_path, dest_path)





main()