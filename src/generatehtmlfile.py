import os
import shutil
from blockparsing import markdown_to_blocks, block_to_block_type, BlockType
from markdowntohtml import markdown_to_html_node


def copy_static(working_dir):
    public_dir = working_dir + "/public"
    static_dir = working_dir + "/static"
    
    clear_target_dir(public_dir)
    copy_dir(static_dir, public_dir)

def clear_target_dir(target_dir):
    contents = os.listdir(target_dir)

    for path in contents:
        abs_path = target_dir + "/" + path
        if os.path.isfile(abs_path):
            os.remove(abs_path)
        else:
            clear_target_dir(abs_path)
            os.rmdir(abs_path)

    print(f"cleared target directory {target_dir}")

def copy_dir(source_dir, target_dir):
    contents = os.listdir(source_dir)

    source_dir_prefix = path_prefix(source_dir)
    target_dir_prefix = path_prefix(target_dir)

    for path in contents:
        abs_path = source_dir + "/" + path

        if os.path.isfile(abs_path):
            file_path = create_target_dir_path(abs_path, source_dir_prefix, target_dir_prefix)
            print(f"created file {file_path}")
            shutil.copy(abs_path, file_path)
        else:
            dir_path = create_target_dir_path(abs_path, source_dir_prefix, target_dir_prefix)
            print(f"created directory {dir_path}")
            os.mkdir(dir_path)
            copy_dir(abs_path, dir_path)


def create_target_dir_path(path, source_prefix, target_prefix):
    return path.replace(source_prefix, target_prefix)

def path_prefix(path):
    path_contents = path.split("/")

    i = -1

    while True:
        if path_contents[i] == ".":
            return path_contents[i + 1]
        
        i -= 1

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        #check if it's a h1
        if block_to_block_type(block) == BlockType.HEADING and block.count("#", 0, 7) == 1:
            block = block.removeprefix("#")
            return block.strip()
    # reached end of markdown without finding a title
    raise ValueError("Error: The markdown file does not contain a h1 heading block for a title and this is required for rendering.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    #read the markdown
    markdown = read_file(from_path)
    template = read_file(template_path)

    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()
    title = extract_title(markdown)

    content = write_title(template, title)
    content = write_content(content, html_content)

    write_file(dest_path, content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    dir_path_prefix = path_prefix(dir_path_content)
    dest_path_prefix = path_prefix(dest_dir_path)

    # read the files in the directory path
    contents = os.listdir(dir_path_content) 
    for path_to_file in contents:
        abs_path = dir_path_content + "/" + path_to_file
        if os.path.isfile(abs_path):
            file_path = create_target_dir_path(abs_path, dir_path_prefix, dest_path_prefix)
            file_path = file_path.replace(".md", ".html")
            generate_page(abs_path, template_path, file_path)
        else:
            #create the directory in the destination directory
            new_dir_path = create_target_dir_path(abs_path, dir_path_prefix, dest_path_prefix)
            os.mkdir(new_dir_path)
            generate_pages_recursive(abs_path, template_path, new_dir_path)
               

def read_file(path_to_file):
    file_contents = ""
    if os.path.isfile(path_to_file):        
        with open(path_to_file) as f:
            file_contents = f.read()  
    else:
        #get the first file in the directory and read that 
        contents = os.listdir(path_to_file) 
        if len(contents) != 0:
            file_contents = read_file(path_to_file + "/" + contents[0])

    return file_contents

def write_title(template, title):
    return template.replace("{{ Title }}", title)

def write_content(template, content):
    return template.replace("{{ Content }}", content)

def write_file(file_path, content):
    try:
        #overwrite the file!
        if not os.path.exists(file_path):
            with open(file_path, "w+") as f:
                f.write(content)        
        else:
            with open(file_path, "w+") as f:
                f.write(content)

        return f'Successfully wrote to "{file_path}"'
    except Exception as e:
        print("Error: error writing the file")
        