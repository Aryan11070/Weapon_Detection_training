import os

image_files = []
os.chdir(os.path.join("valid", "images"))   # go into valid/images

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_files.append("valid/images/" + filename)

os.chdir("../..")   # go back to dataset root

with open("test.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image + "\n")
