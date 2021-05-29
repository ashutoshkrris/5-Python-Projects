import os


def rename_files(path):
    i = 0
    for file in os.listdir(path):
        new_name = f"Hello{i}.txt"
        src = path+file
        new_name = path+new_name
        os.rename(src, new_name)
        i += 1


if __name__ == "__main__":
    rename_files("Renaming-Bulk-Files/demo/")
