import tkinter as tk
from tkinter import filedialog, messagebox as msgbox
from PIL import Image, ImageTk
import detector
import os
import embedder

if not detector.load_detector():
    msgbox.showwarning("Warning", "Model could not be loaded.\nDetection may not work.")


# ---------------- GUI Helper Functions ---------------- #
def heading(c, text, canvas_width, y, colors=["#00f6ff","#8b5cf6"]):
    fnt = ("Consolas", 28, "bold")
    totalChars = len(text)
    x = (canvas_width - totalChars*16)//2
    for i in range(totalChars):
        ch = text[i]
        r = int(int(colors[0][1:3],16)+(int(colors[1][1:3],16)-int(colors[0][1:3],16))*i/totalChars)
        g = int(int(colors[0][3:5],16)+(int(colors[1][3:5],16)-int(colors[0][3:5],16))*i/totalChars)
        b = int(int(colors[0][5:7],16)+(int(colors[1][5:7],16)-int(colors[0][5:7],16))*i/totalChars)
        col = "#%02x%02x%02x" % (r,g,b)
        c.create_text(x, y, text=ch, fill=col, font=fnt, anchor="nw")
        x += 16

def button(p, txt, c1, c2, cmd):
    b = tk.Label(p, text=txt, bg=c1, fg="black", font=("Segoe UI",13,"bold"),
                 width=18, pady=8, cursor="hand2", relief="flat", bd=0)
    b.bind("<Enter>", lambda e: b.config(bg=c2))
    b.bind("<Leave>", lambda e: b.config(bg=c1))
    b.bind("<Button-1>", lambda e: cmd())
    return b

# ---------------- Detector Tab ---------------- #
def uploadImage():
    global i, k, imgLabel
    p = filedialog.askopenfilename(filetypes=[("Images","*.png *.jpg *.jpeg *.bmp")])
    if not p: return
    i = p
    img = Image.open(i).resize((450,300))
    k = ImageTk.PhotoImage(img)
    imgLabel.config(image=k)
    imgLabel.image = k
    output("📁 Selected: " + os.path.basename(i))

def detectImage():
    global i
    if i is None:
        msgbox.showwarning("Warning", "Please upload an image first")
        return
    res = detector.detect_steg(i)
    output("🔎 Result:\n" + res, True)

def output(txt, resize=False):
    outBox.config(state="normal")
    outBox.delete("1.0", tk.END)
    outBox.insert(tk.END, txt)
    if resize:
        l = txt.count("\n")+1
        outBox["height"] = min(max(l,3),6)
    outBox.config(state="disabled")

# ---------------- Etab (Embed Tab) ---------------- #
def openEtab():
    etab = tk.Toplevel()
    etab.title("LSB Stegnography Embedder")
    etab.geometry("850x650")
    etab.configure(bg="#0f111b")

    header = tk.Canvas(etab, width=850, height=80, bg="#0f111b", highlightthickness=0)
    header.pack()
    heading(header, "LSB Stegnography Embedder", 850, 20)

    fImg = tk.Frame(etab, bg="#1c1f2b", bd=2, highlightthickness=4, highlightbackground="#00eaff")
    fImg.pack(pady=(10,15))  # Increased spacing between image container and buttons
    embedImgLabel = tk.Label(fImg, bg="#1c1f2b")
    embedImgLabel.pack(padx=10, pady=10)

    bFrame = tk.Frame(etab, bg="#0f111b")
    bFrame.pack(pady=(5,10))

    embedOut = tk.Text(etab, width=65, height=2, font=("Consolas",12),
                       bg="#111827", fg="#7dd3fc", insertbackground="white",
                       relief="flat", bd=3, highlightthickness=2, highlightbackground="#00eaff", wrap=tk.WORD)
    embedOut.pack(pady=(15,15))
    embedOut.insert(tk.END, "Upload an image to embed...\n")
    embedOut.config(state="disabled")

    def uploadEmbed():
        p = filedialog.askopenfilename(filetypes=[("Images","*.png *.jpg *.jpeg *.bmp")])
        if not p: return
        etab.imgPath = p
        img = Image.open(p).resize((450,300))
        etab.tkImg = ImageTk.PhotoImage(img)
        embedImgLabel.config(image=etab.tkImg)
        embedOut.config(state="normal")
        embedOut.delete("1.0", tk.END)
        embedOut.insert(tk.END, f"📁 Selected: {os.path.basename(p)}")
        embedOut.config(state="disabled")

    def downloadEmb():
        if not hasattr(etab, "imgPath"):
            msgbox.showwarning("Warning", "Upload an image first!")
            return
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image","*.png")])
        if not save_path: return
        lsb_img = embedder.embed_lsb(etab.imgPath, payload_ratio=0.5)
        lsb_img.save(save_path)
        msgbox.showinfo("Success", f"Image saved at:\n{save_path}")

    button(bFrame, "📤 Upload Image", "#4ade80", "#22c55e", uploadEmbed).grid(row=0, column=0, padx=10)
    button(bFrame, "💾 Download", "#ec4899", "#db2777", downloadEmb).grid(row=0, column=1, padx=10)

# ---------------- Main GUI ---------------- #
def setupGUI():
    
    global i, imgLabel, outBox
    i = None
    r = tk.Tk()
    r.title("LSB Stegnography Detector")
    r.geometry("850x650")
    r.configure(bg="#0f111b")

    header = tk.Canvas(r, width=850, height=80, bg="#0f111b", highlightthickness=0)
    header.pack()
    heading(header, "LSB Stegnography Detector", 850, 20)

    fImg = tk.Frame(r, bg="#1c1f2b", bd=2, highlightthickness=4, highlightbackground="#00eaff")
    fImg.pack(pady=(10,15))  # Increased spacing
    imgLabel = tk.Label(fImg, bg="#1c1f2b")
    imgLabel.pack(padx=10, pady=10)

    bFrame = tk.Frame(r, bg="#0f111b")
    bFrame.pack(pady=(5,15))
    button(bFrame, "📤 Upload Image", "#4ade80", "#22c55e", uploadImage).grid(row=0, column=0, padx=10)
    button(bFrame, "🔎 Run Detection", "#60a5fa", "#3b82f6", detectImage).grid(row=0, column=1, padx=10)
    button(bFrame, "📝 Etab", "#ec4899", "#db2777", openEtab).grid(row=0, column=2, padx=10)

    outBox = tk.Text(r, width=65, height=2, font=("Consolas",12), bg="#111827", fg="#7dd3fc",
                     insertbackground="white", relief="flat", bd=3, highlightthickness=2, highlightbackground="#00eaff", wrap=tk.WORD)
    outBox.pack(pady=(15,15))
    outBox.insert(tk.END, "Upload an image to start detection..\n")
    outBox.config(state="disabled")

    r.mainloop()

def main():
    setupGUI()

main()
