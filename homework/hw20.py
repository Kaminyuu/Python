import os

# dirs = [r'folder\test', r'folder\test1']
# for d in dirs:
#     os.makedirs(d)


files = ["project.txt", "test.txt"]
for f in files:
    file = os.path.join("folder", f)
    open(file, "w").close()

files_with_text = [r'folder\project.txt', r'folder\test.txt']
for i in files_with_text:
    with open(i, "w") as f:
        f.write(f"текст файла {i}")


def detecte(root):
    objs = os.listdir(root)
    for n in objs:
        m = os.path.join(root, n)
        if os.path.isfile(m):
            print(f"{os.path.split(m)[1]} - file - {os.path.getsize(m)} - bytes")
        elif os.path.isdir(m):
            print(f"{os.path.split(m)[1]} - dir")


detecte("folder")

