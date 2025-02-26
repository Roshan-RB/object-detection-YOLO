import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image

# Load the trained YOLOv8 model
model_path = r"C:\ML_Apps\object_detection_project\data\pascal_voc\runs\detect\train4\weights\best.pt"
model = YOLO(model_path)

# Streamlit App
st.title("YOLOv8 Object Detection App 🚀")
st.write("Upload an image to detect objects.")

# Upload Image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert the uploaded file to an OpenCV image
    image = Image.open(uploaded_file)
    image = np.array(image)
    
    # Perform inference
    results = model(image)

    # Draw bounding boxes
    for result in results:
        image_with_boxes = result.plot()  # Draw boxes on the image

    # Display results
    st.image(image_with_boxes, caption="Detected Objects", use_column_width=True)

    # Option to save output
    save_option = st.checkbox("Save Output Image")
    if save_option:
        output_path = "output.jpg"
        cv2.imwrite(output_path, cv2.cvtColor(image_with_boxes, cv2.COLOR_RGB2BGR))
        st.success(f"Output saved as {output_path}")
