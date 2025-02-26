# **YOLOv8 Object Detection - Pascal VOC**

This repository demonstrates **object detection** using **YOLOv8**, trained on the **Pascal VOC dataset**. The goal of this project was to understand the basics of **YOLO training pipeline**, from **data preparation to model deployment**.

---

## **1. Project Overview**
- Trains **YOLOv8** on the **Pascal VOC dataset**.
- Covers **data preparation**, **model training**, **evaluation**, **inference**, and **deployment**.
- Deploys a **Streamlit web app** to detect objects in uploaded images.

---

## **2. Folder Structure**
```
object_detection_project/
│── models/               # Trained YOLOv8 model
│   ├── best.pt           # Best model from training
│── src/                  # Source code
│   ├── app.py            # Streamlit app for object detection
│   ├── infer.py          # Inference script
│── .gitignore            # Ignored files
│── README.md             # Project documentation
│── requirements.txt      # Dependencies
```

---

## **3. Setup Instructions**

### **3.1 Install Dependencies**
Clone the repository and install the required libraries:
```bash
git clone <YOUR_GITHUB_REPO>
cd object_detection_project
pip install -r requirements.txt
```

### **3.2 Download Pascal VOC Dataset**
1. Download the **Pascal VOC 2012 dataset**:
   ```bash
   mkdir data/pascal_voc
   cd data/pascal_voc
   wget http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
   tar -xf VOCtrainval_11-May-2012.tar
   ```
2. Convert **VOC annotations to YOLO format**:
   ```bash
   python src/convert_voc_to_yolo.py
   ```
3. Split dataset into **train** and **validation**:
   ```bash
   python src/split_data.py
   ```

---

## **4. Training the YOLOv8 Model**
Run the following command to train YOLOv8:
```bash
yolo task=detect mode=train model=yolov8n.pt data=data/pascal_voc/voc.yaml epochs=20 imgsz=320 device=0
```
- `epochs=20`: Number of training epochs.
- `imgsz=320`: Image size.
- `device=0`: Use GPU (if available).

The trained model will be saved in:
```
runs/detect/train/weights/best.pt
```

---

## **5. Model Evaluation**
After training, evaluate the model on the validation set:
```bash
yolo task=detect mode=val model=runs/detect/train/weights/best.pt data=data/pascal_voc/voc.yaml
```
This outputs:
- **Precision, Recall, and mAP@50 scores**.
- Performance for each class in Pascal VOC.

---

## **6. Running Inference**
### **6.1 Inference on a Single Image**
```bash
yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source=bus.jpg
```

### **6.2 Inference on a Folder of Images**
```bash
yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source=data/pascal_voc/VOCdevkit/VOC2012/JPEGImages save=True
```

### **6.3 Run Inference in Python**
Use the provided script to run inference inside Python:
```bash
python src/infer.py
```

---

## **7. Deploying the Model with Streamlit**
To run the **Streamlit web app**, execute:
```bash
streamlit run src/app.py
```
This will:
- Start a local web app.
- Allow users to upload images for object detection.

---

## **8. Next Steps**
This project serves as a **foundation** for YOLO-based object detection. You can:
- Train on a **different dataset**.
- Use **YOLOv8m or YOLOv8l** for better accuracy.
- Deploy on **cloud platforms** or optimize using **ONNX/TensorRT**.

---

## **9. References**
- [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com/)
- [Pascal VOC Dataset](http://host.robots.ox.ac.uk/pascal/VOC/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

### **Final Notes**
This project was intended as a learning exercise in object detection. If you encounter issues, feel free to raise an **issue** or contribute with improvements.

