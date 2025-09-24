import os

image_files = []
os.chdir(os.path.join("train", "images"))   # go into train/images

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_files.append("train/images/" + filename)

os.chdir("../..")   # go back to dataset root

with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image + "\n")
