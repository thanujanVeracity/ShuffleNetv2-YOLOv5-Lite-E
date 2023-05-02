import os 
import shutil


# Get all the list of files 
files = os.listdir("./photo1")


# Split the files into train and valid 
files.sort()
images = []
labels = []

for f in files:
    if(f.split(".")[1] == "JPG"):
        images.append(f)
    else:
        labels.append(f)

length = len(images)
unit_length = int(length/10)

train_images  = images[:unit_length*8]
train_labels  = labels[:unit_length*8]

valid_images  = images[unit_length*8:length]
valid_labels  = labels[unit_length*8:length]

print(valid_images)
#move the files into the respect directories

# if (os.path.isdir("train") and os.path.isdir("valid")):
os.mkdir("train")
os.mkdir("valid")

train_image_path = "train/images/"
train_label_path = "train/labels/"

valid_image_path = "valid/images/"
valid_label_path = "valid/labels/"

os.mkdir(train_image_path)
os.mkdir(train_label_path)
os.mkdir(valid_label_path)
os.mkdir(valid_image_path)


for i in range(len(train_images)):
    shutil.move("./photo1/" + train_images[i], train_image_path )
    shutil.move("./photo1/" + train_labels[i], train_label_path)

for i in range(len(valid_images)):    
    shutil.move("./photo1/" +valid_images[i], valid_image_path )
    shutil.move("./photo1/" + valid_labels[i], valid_label_path )
