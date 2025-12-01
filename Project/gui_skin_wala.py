#CHANGES K LIYAY LMK WHAT SUGGESTIONS YOU GUYS HAVE YA COLOR SCHEME KO AUR BLEND KRNA CHAHTAY ABHI PHELE INTEGRATE KRLO - its lovely bbg
import tkinter as tk
from tkinter import filedialog, messagebox as msgbox
from PIL import Image, ImageTk
import os
import detector

if not detector.load_detector():
    msgbox.showwarning("Warning", "Model could not be loaded.\nDetection may not work.")

def stegDetect(imgPath):
    if imgPath is None:
        msgbox.showwarning("Warning", "Please upload an image first")
        return
    res = detector.detect_steg(imgPath)
    return "🔎 Result:\n" + res

def uploadImage():
    global imgPath, imgLabelTk, imgName, imgType
    p = filedialog.askopenfilename(filetypes=[("Images","*.png *.jpg *.jpeg *.bmp")])
    if not p: 
     return
    imgPath = p
    imgName = os.path.basename(imgPath)
    imgType = os.path.splitext(imgName)[1][1:].upper()
    img = Image.open(imgPath)
    img = img.resize((350, 240))
    imgLabelTk = ImageTk.PhotoImage(img)
    imgLabel.config(image=imgLabelTk)
    imgLabel.image = imgLabelTk

def detectImage():
    global imgPath
    if imgPath is None:
      msgbox.showwarning("Please upload an image first")
      return
    res = stegDetect(imgPath)
    tB.config(state="normal")   #before u think wth is tb it is text box output wala
    tB.delete("1.0", tk.END)
    tB.tag_configure("center", justify='center', spacing3=10)
    tB.tag_configure("bold", font=("Consolas", 12, "bold"), justify='center', spacing3=10)
    tB.tag_configure("heading", font=("Segoe UI", 14, "bold"), justify='center', spacing3=10)
    tB.insert(tk.END, "\n")
    tB.insert(tk.END, "Detection Output\n\n", "heading")
    tB.insert(tk.END, f"Image Name: {imgName}\n", "center")
    tB.insert(tk.END, f"Image Type: {imgType}\n\n", "center")
    tB.insert(tk.END, f"{res}", "bold")
    tB.config(state="disabled")

def leftContainer(R):
    global imgLabel
    lFrame = tk.Frame(R, bg="#f3dabe")
    lFrame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

    tk.Label(lFrame, text=" LSB Steganography Detector", font=("Segoe UI", 22, "bold"),bg="#f3dabe", fg="#5a3e36").pack(pady=20)
    imgLabel = tk.Label(lFrame, bg="#f3dabe")
    imgLabel.pack(pady=20, padx=15)
    uploadButton = tk.Button(lFrame,text="📤 Upload Image", font=("Segoe UI",12,"bold"),bg="#deb887", fg="#000", width=22, relief="flat", command=uploadImage)
    uploadButton.pack(pady=10)
    detectButton = tk.Button(lFrame, text="🔎 Run Detection", font=("Segoe UI",12,"bold"),bg="#d2b48c", fg="#000", width=22, relief="flat", command=detectImage)
    detectButton.pack(pady=10)

def rightCon(R):
    global tB
    rFrame = tk.Frame(R, bg="#f5e4d7")
    rFrame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
    tB = tk.Text(rFrame, width=40, height=12, font=("Consolas",12),bg="#d2b48c", fg="#3b2f2f", insertbackground="black",
    relief="flat", bd=0)

    tB.place(relx=0.5, rely=0.25, anchor="n")
    tB = tk.Text(rFrame, width=40, height=12, font=("Consolas",12), bg="#d2b48c", fg="#3b2f2f", insertbackground="black",
    relief="flat", bd=0)  #text adjust  to avoid chipa - whats chipa
    tB.place(relx=0.5, rely=0.25, anchor="n")  #oper space
    tB.config(padx=10, pady=10)  

    tB.insert(tk.END, "Upload an image to start detection..\n")
    tB.config(state="disabled")

def main():
    global imgPath, imgName, imgType
    imgPath = None
    imgName = ""
    imgType = ""
    r = tk.Tk()
    r.title("LSB Steganography Detector")
    r.geometry("950x600")
    r.configure(bg="#f2e1d4")
    leftContainer(r)
    rightCon(r)
    r.mainloop()

main()

