import os

DIR = r"C:\Users\roman\Documents\"

def rename_fls(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            rename_f(root, name)

def rename_f(root, name):
    valid_name = get_valid_name(name)
    old_desc = os.path.join(root, name)
    new_desc = os.path.join(root, valid_name)
    os.rename(old_desc, new_desc)

def get_valid_name(name):
    name = name.replace(" ", "")
    name = name.zfill(6)
    return name


if __name__ == "__main__":
    rename_fls(DIR)