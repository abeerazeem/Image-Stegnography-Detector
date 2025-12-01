import os
import gdown
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model

MODEL_URL = "https://drive.google.com/uc?id=1VzU2u0_d8sJLdEOGZ8BtAXcJTA1ZJICx"
MODEL_PATH = "lsb_mobilenetv2_model.h5"

MODEL = None

def download_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model from Google Drive...")
        gdown.download(MODEL_URL, MODEL_PATH, quiet=False, fuzzy=True)
        print("Model downloaded.")

def load_detector():
    global MODEL
    try:
        download_model()
        MODEL = load_model(MODEL_PATH)
        print("Model loaded successfully.")
        return True
    except Exception as e:
        print(f"Model load failed: {e}")
        return False

def preprocess_image(img_path):
    img = Image.open(img_path).convert("RGB")
    img = img.resize((224,224))
    arr = np.array(img) / 255.0
    return np.expand_dims(arr, axis=0)

def detect_steg(img_path):
    if MODEL is None:
        return "⚠ Model not loaded!"
    try:
        img = preprocess_image(img_path)
        pred = MODEL.predict(img)[0][0]
        return " ✅ Clean" if pred > 0.5 else " ⚠️ Steganography Detected"
    except Exception as e:
        return f"Detection Error: {e}"
