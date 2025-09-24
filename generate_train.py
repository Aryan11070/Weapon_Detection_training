import os

image_files = []
for filename in os.listdir("train/images"):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_files.append("train/images/" + filename)

with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image + "\n")
