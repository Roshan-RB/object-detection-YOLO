from ultralytics import YOLO
import cv2

# Load the trained model
model = YOLO("models/best.pt")

# Load and predict on an image
image_path = "example.jpg"  # Change this to any image path
results = model(image_path)

# Show image with detections
for result in results:
    im_array = result.plot()  # Draw bounding boxes
    cv2.imshow("YOLO Inference", im_array)
    cv2.waitKey(0)  # Press any key to close
    cv2.destroyAllWindows()
