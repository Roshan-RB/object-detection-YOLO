import os
import random
import shutil

# Define paths
DATASET_PATH = "../data/pascal_voc/VOCdevkit/VOC2012/"
IMG_PATH = os.path.join(DATASET_PATH, "JPEGImages")
LABEL_PATH = os.path.join(DATASET_PATH, "labels")

# Destination folders
TRAIN_IMG_PATH = os.path.join(DATASET_PATH, "images/train")
VAL_IMG_PATH = os.path.join(DATASET_PATH, "images/val")
TRAIN_LABEL_PATH = os.path.join(DATASET_PATH, "labels/train")
VAL_LABEL_PATH = os.path.join(DATASET_PATH, "labels/val")

# Create directories
os.makedirs(TRAIN_IMG_PATH, exist_ok=True)
os.makedirs(VAL_IMG_PATH, exist_ok=True)
os.makedirs(TRAIN_LABEL_PATH, exist_ok=True)
os.makedirs(VAL_LABEL_PATH, exist_ok=True)

# Get list of image files
image_files = [f for f in os.listdir(IMG_PATH) if f.endswith(".jpg")]

# Shuffle and split
random.shuffle(image_files)
split_ratio = 0.8
train_size = int(len(image_files) * split_ratio)

train_files = image_files[:train_size]
val_files = image_files[train_size:]

# Move files to train/val directories
def move_files(file_list, src_img_path, src_label_path, dest_img_path, dest_label_path):
    for file in file_list:
        img_src = os.path.join(src_img_path, file)
        label_src = os.path.join(src_label_path, file.replace(".jpg", ".txt"))
        
        img_dest = os.path.join(dest_img_path, file)
        label_dest = os.path.join(dest_label_path, file.replace(".jpg", ".txt"))
        
        shutil.move(img_src, img_dest)
        if os.path.exists(label_src):  # Move labels only if they exist
            shutil.move(label_src, label_dest)

move_files(train_files, IMG_PATH, LABEL_PATH, TRAIN_IMG_PATH, TRAIN_LABEL_PATH)
move_files(val_files, IMG_PATH, LABEL_PATH, VAL_IMG_PATH, VAL_LABEL_PATH)

print(f"✅ Dataset split complete: {len(train_files)} train, {len(val_files)} val")
