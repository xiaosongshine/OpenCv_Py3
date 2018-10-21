
import os

file_dir = r"../att_faces"

datas = os.walk(file_dir)

items = []


for root, dirs, files in datas:

    if (len(dirs) == 0):
        for i in range(len(files)):
            str1 = root+"/"+files[i]
            id = root.split(r"/s")
            items.append(str1+","+id[1])

print(items)

def save_to_file(file_path_name, contents):
    fh = open(file_path_name, "a")
    fh.write(contents)

    fh.close()
for j in range(len(items)):
    save_to_file("lables.csv", items[j]+"\n")