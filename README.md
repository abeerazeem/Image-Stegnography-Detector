# LSB Image StegnographyDetector App

A Python-based Image Steganography Detector with a Graphical User Interface (GUI) built using Tkinter.

---

## 📁 Project Structure

Ensure your directory contains the following files:

```
Project/
│
├── gui.py
├── detector.py
└── requirements.txt
```

---

## 🐍 Python Version Requirement

You must have:

**Python 3.8 or higher**  
Recommended version: **Python 3.9 or 3.10**

Check your Python version:

```bash
python --version
```

or

```bash
python3 --version
```

---

## 🛠️ Step 1: Create a Virtual Environment (Recommended)

### ✅ Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### ✅ Windows (Command Prompt / PowerShell)

```bash
python -m venv venv
venv\Scripts\activate
```

After activation, you should see:

```
(venv)
```

---

## 📦 Step 2: Install Dependencies

Install all required libraries:

```bash
pip install -r requirements.txt
```

If installation fails:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ▶️ Step 3: Run the Application

Launch the GUI:

```bash
python gui.py
```

or on Linux/macOS:

```bash
python3 gui.py
```

---

## 🧯 Common Issues and Fixes

### ❌ Tkinter Not Found (Linux)

Install Tkinter:

```bash
sudo apt install python3-tk
```

Windows/macOS users should reinstall Python and ensure Tkinter is installed.

---

### ❌ ModuleNotFoundError

Ensure:

- Virtual environment is activated  
- Requirements are installed  
- Correct Python version is used  

---

### ❌ Model Not Found Error

If a trained model is required:

- Check the model file location  
- Verify file path in `detector.py`  

---

## 💻 Recommended Operating Systems

This project works on:

- Linux  
- Windows  
- macOS  

---

## 🚀 Quick Start (All-in-One)

```bash
git clone https://github.com/abeerazeem/Image-Stegnography-Detector
cd Project
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python gui.py #On Linux: python3 gui.py
```

---

If you experience issues, create a GitHub Issue or contact the contributers.







