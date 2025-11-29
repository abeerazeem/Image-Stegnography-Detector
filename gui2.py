import tkinter as tk
from tkinter import filedialog, messagebox as msgbox
from PIL import Image, ImageTk
import os

def stegDetector(img): 
  return "No hidden data detected"

def heading(c, text, canvas_width, y):
    fnt = ("Segoe UI", 28, "bold")
    totalChars = len(text)
    x = (canvas_width - totalChars*18)//2
    colors = ["#00f6ff","#8b5cf6"]
    for i in range(totalChars):
        ch = text[i]
        r = int(int(colors[0][1:3],16)+(int(colors[1][1:3],16)-int(colors[0][1:3],16))*i/totalChars)
        g = int(int(colors[0][3:5],16)+(int(colors[1][3:5],16)-int(colors[0][3:5],16))*i/totalChars)
        b = int(int(colors[0][5:7],16)+(int(colors[1][5:7],16)-int(colors[0][5:7],16))*i/totalChars)
        col = "#%02x%02x%02x" % (r,g,b)
        c.create_text(x, y, text=ch, fill=col, font=fnt, anchor="nw")
        x += 18

def button(p, txt, c1, c2, cmd):
    b = tk.Label(p, text=txt, bg=c1, fg="black",font=("Segoe UI",13,"bold"), width=18, pady=8, cursor="hand2", relief="flat", bd=0)
    b.bind("<Enter>", lambda e: b.config(bg=c2))
    b.bind("<Leave>", lambda e: b.config(bg=c1))
    b.bind("<Button-1>", lambda e: cmd())
    return b

def uploadImage():
    global i, k
    p = filedialog.askopenfilename(filetypes=[("Images","*.png *.jpg *.jpeg *.bmp")])
    if not p:
        return
    i = p
    im = Image.open(i)
    im = im.resize((450,300))
    k = ImageTk.PhotoImage(im)
    imgLabel.config(image=k)
    imgLabel.image = k
    output("📁 Selected: " + os.path.basename(i))

def detectImage():
    if i is None:
        msgbox.showwarning("Please upload an image first")
        return
    res = stegDetector(i)
    output("🔎 Result:\n" + res, True)

def output(txt, resize=False):
    outBox.config(state="normal")
    outBox.delete("1.0", tk.END)
    outBox.insert(tk.END, txt)
    if resize:
        l = txt.count("\n")+1
        if l < 3: outBox["height"] = 3
        elif l > 6: outBox["height"] = 6
        else: outBox["height"] = l
    outBox.config(state="disabled")

def setupGUI():
    global i, imgLabel, outBox, upButton, detectButton, k
    i = None
    r = tk.Tk()
    r.title("Stegnography Detector")
    r.geometry("850x650")
    r["bg"] = "#0f111b"

    head = tk.Canvas(r, width=850, height=80, bg="#0f111b", highlightthickness=0)
    head.pack()
    heading(head, "Stegnography Detector", 850, 20)

    fImg = tk.Frame(r, bg="#1c1f2b", bd=2, highlightthickness=4, highlightbackground="#00eaff")
    fImg.pack(pady=10)
    imgLabel = tk.Label(fImg, bg="#1c1f2b")
    imgLabel.pack(padx=10, pady=10)

    bFrame = tk.Frame(r, bg="#0f111b")
    bFrame.pack(pady=5)
    upButton = button(bFrame, "📤 Upload Image", "#4ade80", "#22c55e", uploadImage)
    upButton.grid(row=0, column=0, padx=10)
    detectButton = button(bFrame, "🔎 Run Detection", "#60a5fa", "#3b82f6", detectImage)
    detectButton.grid(row=0, column=1, padx=10)
    tk.Label(r, text="Detection Output", fg="#00eaff", bg="#0f111b", font=("Segoe UI",14,"bold")).pack(pady=(10,2))
    
    global outBox
    outBox = tk.Text(r, width=70, height=2, font=("Consolas",12), bg="#111827", fg="#7dd3fc",
    insertbackground="white", relief="flat", bd=3, highlightthickness=2, highlightbackground="#00eaff", wrap=tk.WORD)
    outBox.pack(pady=(0,15))
    outBox.insert(tk.END, "Upload an image to start detection..\n")
    outBox.config(state="disabled")

    r.mainloop()

def main():
    setupGUI()

main()
