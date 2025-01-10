import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import base64

# Set the browser tab title and favicon
st.set_page_config(
    page_title="Waste Classification System",  # App name
    page_icon="♻️",  # Favicon set to recycling emoji
    layout="wide"  # Wide layout for better spacing
)

# Function to set a background image
def set_background(image_file):
    # Encode image to base64
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()

    # Inject CSS with base64 image as background
    st.markdown(
        f"""
        <style>
        /* General Styling */
        .block-container {{
            padding-top: 0px !important;
            padding-bottom: 0px !important;
        }}
        header {{
            visibility: hidden; /* Hide header */
        }}
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
        }}
        /* Text Styling */
        .stText, .stMarkdown {{
            color: white !important;  /* White text for description */
            font-weight: bold;  /* Making the text bold */
            font-size: 18px;  /* Improved text size for readability */
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); /* Adding text shadow for better contrast */
        }}
        /* Page Title Styling */
        .stTitle {{
            font-family: 'Arial', sans-serif;
            font-weight: bold;
            font-size: 48px;
            color: black !important;  /* Black for the page title */
            text-align: center;
            text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.7); /* Text shadow */
        }}
        /* Smaller text styling for description */
        .stDescription {{
            color: black !important;
            font-size: 14px !important; /* Smaller font size for the description */
            text-shadow: none;
            font-weight: normal;
            text-align: center;
        }}
        /* Category Titles Color */
        .HazardousWaste {{
            color: red !important;
        }}
        .NonRecyclableWaste {{
            color: #FF8C00 !important; /* Orange color */
        }}
        .RecyclableWaste {{
            color: blue !important;
        }}
        .OrganicWaste {{
            color: green !important;
        }}
        /* Results Section Styling */
        .result-text {{
            font-size: 30px;
            font-weight: bold;
            padding: 20px;
            text-align: center;
            border-radius: 10px;
            margin-top: 20px;
            background-color: rgba(0, 0, 0, 0.5);  /* Semi-transparent background */
        }}
        .info-text {{
            font-size: 20px;
            color: white;  /* White text color */
            background-color: rgba(0, 0, 0, 0.5);  /* Semi-transparent background */
            padding: 15px;
            border-radius: 10px;
            margin-top: 10px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }}
        .stButton {{
            background-color: #32CD32;
            color: white;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        }}
        .stFileUploader {{
            border: 2px solid #32CD32;
            padding: 10px;
            background-color: rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            color: #fff;
            font-size: 18px;
        }}
        .stFileUploader:hover {{
            background-color: rgba(0, 0, 0, 0.4);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply the background image (update with the correct path to your image)
set_background("recycling-program-green-waste-management-260nw-2461809723.jpg")

# Load the pre-trained model
model = load_model('model.h5')

# Define subcategories for each top-level category
sub_categories = {
    'Hazardous': ['Battery', 'Biological'],
    'Non-Recyclable': ['Shoes', 'Trash', 'Clothes'],
    'Recyclable': ['White Glass', 'Brown Glass', 'Metal', 'Green Glass', 'Plastic'],
    'Organic': ['Cardboard', 'Paper']
}

# Function to preprocess the image
def preprocess_image(img_path):
    img = Image.open(img_path)
    img = img.resize((224, 224))  # Resize to model input size
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Function to predict the top-level category and sub-category
def predict_top_level(img_path):
    img_array = preprocess_image(img_path)
    top_level_pred, sub_category_pred = model.predict(img_array)

    top_level_category = np.argmax(top_level_pred, axis=1)[0]
    top_level_categories = ['Hazardous', 'Non-Recyclable', 'Organic', 'Recyclable']
    top_level_label = top_level_categories[top_level_category]

    top_level_confidence = max(top_level_pred[0]) * 100  # Confidence of top-level prediction

    # Dynamically select subcategories based on top-level category
    sub_categories_for_top_level = sub_categories[top_level_label]
    sub_category_pred_filtered = sub_category_pred[:, :len(sub_categories_for_top_level)]
    sub_category = np.argmax(sub_category_pred_filtered, axis=1)[0]
    sub_category_confidence = max(sub_category_pred_filtered[0]) * 100
    sub_category_label = sub_categories_for_top_level[sub_category]

    if sub_category_confidence < 40:
        sub_category_label = "Uncertain Prediction"
        sub_category_message = f"The item is identified as part of the `{top_level_label}` category, which could be `{', '.join(sub_categories_for_top_level)}`, but the exact sub-category is uncertain."
    else:
        sub_category_message = ""

    return top_level_label, sub_category_label, top_level_confidence, sub_category_confidence, sub_category_message

# Waste disposal recommendations for each category
disposal_instructions = {
    'Hazardous': {
        'title': 'Hazardous Waste 🚨',
        'steps': [
            '🔋 **Batteries**: Dispose of used batteries at specialized **hazardous waste collection centers**. These facilities are equipped to handle potentially dangerous chemicals and components safely.',
            '💉 **Biological Waste**: **Contact medical waste disposal services** to handle biological waste safely. These services ensure that hazardous materials such as medical needles are handled with care to avoid contamination.',
            '🔬 **E-Waste**: Old electronics can contain harmful substances such as mercury and lead. **Take e-waste to certified e-waste recycling centers** to ensure safe disposal and recycling.'
        ]
    },
    'Non-Recyclable': {
        'title': 'Non-Recyclable Waste 🚯',
        'steps': [
            '🚮 **Plastic Bags**: These should never be thrown into recycling bins as they contaminate the recycling process. **Dispose of them in trash bins**.',
            '🩳 **Clothes**: If they are no longer wearable, **donate them to charities** or dispose of them in textile recycling bins.',
            '👠 **Shoes**: **Recycle footwear** at designated recycling stations or **donate** gently used shoes to charities to avoid waste accumulation.'
        ]
    },
    'Recyclable': {
        'title': 'Recyclable Waste ♻️',
        'steps': [
            '🗑️ **Plastic**: Clean and remove any food residue. **Place the plastic in designated recycling bins**. Opt for **reusable containers** to reduce plastic waste.',
            '🍶 **Glass**: Ensure the glass items are free of contaminants and **place them in glass recycling containers**. Recycling glass saves energy and reduces the need for raw materials.',
            '🔩 **Metal**: Rinse metal items to remove food residue. **Recycle metal cans** and other items to reduce energy consumption and preserve natural resources.'
        ]
    },
    'Organic': {
        'title': 'Organic Waste 🌱',
        'steps': [
            '🍂 **Yard Waste**: Collect leaves, grass clippings, and other yard waste in a compost bin. **Composting organic waste** reduces landfill waste and enriches the soil.',
            '📦 **Cardboard & Paper**: Flatten cardboard boxes and dispose of them in paper recycling bins. **Recycling paper saves trees**, and **ensures paper products are reprocessed** for new use.'
        ]
    }
}

# Streamlit app title
st.markdown("<h2 class='stTitle'>Waste Classification System</h2>", unsafe_allow_html=True)
st.markdown("<h3 class='stDescription'>Upload an image to classify its waste category and learn how to dispose of it correctly.</h3>", unsafe_allow_html=True)

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Split the screen into two columns for image on the left and predictions on the right
    col1, col2 = st.columns([1, 2])  # 1: image, 2: predictions and text

    with col1:
        # Display image with a fixed width
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image', use_container_width=True)  # Removed deprecated parameter

    with col2:
        # Predict top-level category and subcategory
        top_level, sub_category, top_level_confidence, sub_category_confidence, sub_category_message = predict_top_level(uploaded_file)

        # Show results with different colors based on top-level category
        st.markdown(f"<h3 class='{top_level}Waste'>{top_level} Waste</h3>", unsafe_allow_html=True)
        st.markdown(f"**Top-Level Confidence:** {top_level_confidence:.2f}%")

        if sub_category != "Uncertain Prediction":
            st.write(f"**Sub-Category:** {sub_category}")
            st.write(f"**Sub-Category Confidence:** {sub_category_confidence:.2f}%")
        else:
            st.write(f"**Sub-Category:** {sub_category}")
            st.write(sub_category_message)

        # Waste disposal instructions
        st.write(f"\n**Disposal Instructions for {top_level} Waste**:")
        st.write(f"### {disposal_instructions[top_level]['title']}")
        
        for step in disposal_instructions[top_level]['steps']:
            st.write(step)
