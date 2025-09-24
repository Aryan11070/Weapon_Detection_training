import os

image_files = []
for filename in os.listdir("valid/images"):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_files.append("valid/images/" + filename)

with open("test.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image + "\n")
