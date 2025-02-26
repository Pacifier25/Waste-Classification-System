## 🌟 Overview

The **Waste Classification System** is an AI-powered tool designed to classify household waste into different categories, enabling effective recycling and waste management. By leveraging advanced deep learning models, the system simplifies waste segregation, ensuring accurate classification for improved recycling processes.

With support for both image uploads and real-time camera-based classification, the system is user-friendly and accessible. It minimizes errors in waste sorting, promotes responsible disposal practices, and contributes to environmental conservation efforts by reducing landfill waste and supporting sustainable resource management.

### 📊 Dataset

The dataset used in this project consists of 15,150 images, originally categorized into 12 different waste classes. These classes were grouped into 4 broader categories based on their characteristics:

- **Hazardous Waste**: battery, biological  
- **Non-Recyclable Waste**: clothes, shoes, trash  
- **Organic Waste**: cardboard, paper  
- **Recyclable Waste**: brown-glass, green-glass, metal, plastic, white-glass
  
This grouping simplifies the classification process while maintaining the essence of the dataset.
These images have been collected using web scraping techniques for various types of garbage. The goal is to classify the waste into appropriate categories for recycling.
The dataset provides a broader variety of images, which helps improve the classification and recycling accuracy.

### 🧠 Model

The system uses **ResNet50**, a powerful pre-trained Convolutional Neural Network (CNN) model. ResNet50 is fine-tuned to classify the images based on their waste categories. The model is trained on the waste images, yielding highly accurate results.  

### 🏅 Performance

- **Training Accuracy**: 99.81%
- **Validation Accuracy**: 98.62%

---

## 🎯 Features

- **Upload Image**: Users can upload waste images in `.jpg`, `.png`, or `.jpeg` format for classification.  
- **AI-Powered Classification**: The model uses deep learning to classify images into one of the defined categories.  
- **Real-Time Feedback**: Displays the classification result and confidence percentage instantly.  
- **User-Friendly Interface**: Built using **Streamlit**, providing an easy-to-use platform for users to interact with the model.

---

## 🛠️ Technology Stack

- **Programming Language**: Python  
- **Deep Learning Framework**: TensorFlow/Keras  
- **Frontend Framework**: Streamlit  
- **Deployment**: GitHub (currently), upcoming deployment on Microsoft Azure

---

## 📂 Folder Structure
```
├── app.py 
├── requirements.txt 
├── model 
├── waste_classification_model.h5 
└── README.md
```

---

## 📊 Results

- **Final Training Accuracy**: **99.81%**  
- **Final Validation Accuracy**: **98.62%**  
- **Model Type**: ResNet50 (Fine-tuned for this dataset)  
- **Dataset Used**: Custom Waste Dataset

---

## 📊 Visualizations

### **Training vs Validation Loss**
![Training vs Validation Loss](https://github.com/user-attachments/assets/eb2e46bd-4f41-45ed-9f34-2186998a63df)

### **Training vs Validation Accuracy**
![Training vs Validation Accuracy](https://github.com/user-attachments/assets/9eb701c3-9ddd-4906-9f95-d28809569d04)

---


## 🎥 Demo Video
[Watch Demo Video](https://drive.google.com/file/d/1XBXA0wtbkkW88lU5drZ4z9-CepL-8ccW/view?usp=sharing)

---

## 💻 Installation Guide

### Prerequisites
- **Python** 3.7 or later  
- **Virtual Environment** (optional)  

### Steps
1. **Clone the Repository**:
```bash
git clone https://github.com/Pacifier25/Waste-Classification-System.git
cd Waste-Classification-System
```
2. **Create Virtual Environment**:
```bash
Copy code
python -m venv env
source env/bin/activate      # For Linux/Mac
env\Scripts\activate         # For Windows
```

3. **Install Dependencies**:
```bash
pip install -r project_files/requirements.txt
```

4. **Run the Application**:
```bash
streamlit run app.py
```
---
## 🚀 Deployment
The application is deployed using Streamlit for easy web access. Future plans include deploying the project on Microsoft Azure for better scalability.

---

## 📥 Download
**[Click here to download the project files](https://github.com/Pacifier25/Waste-Classification-System/archive/refs/heads/main.zip)**

---

## 🙏 Acknowledgements
- **Dataset**: [Garbage_classification](https://www.kaggle.com/datasets/mostafaabla/garbage-classification).
- **Model**: ResNet50, a pre-trained deep learning model from Keras.
- **Frameworks**: TensorFlow, Streamlit

---

This `README.md` file includes sections for project description, dataset details, model used, accuracy, features, technology stack, folder structure, results, installation guide, and deployment details.

