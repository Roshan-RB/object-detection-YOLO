import os
import xml.etree.ElementTree as ET

# Define paths
VOC_PATH = "../data/pascal_voc/VOCdevkit/VOC2012/"
ANNOTATIONS_PATH = os.path.join(VOC_PATH, "Annotations")
IMAGES_PATH = os.path.join(VOC_PATH, "JPEGImages")
YOLO_LABELS_PATH = os.path.join(VOC_PATH, "labels")

# Create labels folder
os.makedirs(YOLO_LABELS_PATH, exist_ok=True)

# Class names from Pascal VOC
CLASS_NAMES = [
    "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair",
    "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant",
    "sheep", "sofa", "train", "tvmonitor"
]

# Convert VOC XML to YOLO format
def convert_annotation(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    img_filename = root.find("filename").text
    img_width = float(root.find("size/width").text)
    img_height = float(root.find("size/height").text)

    yolo_labels = []
    
    for obj in root.findall("object"):
        cls_name = obj.find("name").text
        if cls_name not in CLASS_NAMES:
            continue
        cls_id = CLASS_NAMES.index(cls_name)
        
        bbox = obj.find("bndbox")
        x_min = float(bbox.find("xmin").text)
        y_min = float(bbox.find("ymin").text)
        x_max = float(bbox.find("xmax").text)
        y_max = float(bbox.find("ymax").text)
        
        # Convert to YOLO format (normalized)
        x_center = (x_min + x_max) / (2.0 * img_width)
        y_center = (y_min + y_max) / (2.0 * img_height)
        width = (x_max - x_min) / img_width
        height = (y_max - y_min) / img_height

        yolo_labels.append(f"{cls_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

    # Save to file
    yolo_label_file = os.path.join(YOLO_LABELS_PATH, img_filename.replace(".jpg", ".txt"))
    with open(yolo_label_file, "w") as f:
        f.write("\n".join(yolo_labels))

# Process all XML files
xml_files = [f for f in os.listdir(ANNOTATIONS_PATH) if f.endswith(".xml")]
for xml_file in xml_files:
    convert_annotation(os.path.join(ANNOTATIONS_PATH, xml_file))

print("VOC to YOLO conversion complete! Labels saved in 'labels/'")
