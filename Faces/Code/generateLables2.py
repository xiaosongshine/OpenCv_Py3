
import os

file_dir = r"../att_faces"

root1 = os.listdir(file_dir)



def printInfo(input):
    print(type(input))
    print(len(input))
    #print(input.shape)
    print(input)

#printInfo(root1)
items = []
files = []
pathfile = []
for j in range(len(root1)):

    files = os.listdir(file_dir + r"/" + root1[j])
    #printInfo(files[j])
    for i in range(len(files)):
        subfile = file_dir + r"/" + root1[j] + r"/" + files[i]
        ids = root1[j].split(R"s")#raw
        id = ids[-1]
        subfile += "," + id
        items.append(subfile)








def save_to_file(file_path_name, contents):
    fh = open(file_path_name, "a")
    fh.write(contents)

    fh.close()
for j in range(len(items)):
    save_to_file("lables3.csv", items[j]+"\n")

print("store Ok")