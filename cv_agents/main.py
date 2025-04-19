import shutil
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def upload_file():
    file_path = filedialog.askopenfilename(
        title="Select Resume File",
        filetypes=[("Resume Files", "*.pdf *.docx")]
    )

    if not file_path:
        return

    try:
        dest_folder = "resumes"
        os.makedirs(dest_folder, exist_ok=True)
        file_name = os.path.basename(file_path)
        dest_path = os.path.join(dest_folder, file_name)

        shutil.copy(file_path, dest_path)
        messagebox.showinfo(" Success", f"Resume uploaded to '{dest_folder}'")

        # Run full pipeline
        root.after(2000, lambda: [root.destroy(), run_pipeline()])

    except Exception as e:
        messagebox.showerror(" Error", f"Something went wrong:\n{e}")

def run_pipeline():
    try:
        subprocess.run(["python", "cv_agents/resume_collector.py"], check=True)
        subprocess.run(["python", "cv_agents/resume_scorer.py"], check=True)
        subprocess.run(["python", "cv_agents/email_sender.py"], check=True)

        messagebox.showinfo(" Done", "Message successfully sent")
    except subprocess.CalledProcessError as e:
        messagebox.showerror(" Pipeline Error", f"An error occurred while running:\n{e}")

# GUI setup
root = tk.Tk()
root.title(" Resume Uploader")
root.geometry("400x200")
root.resizable(False, False)

title_label = tk.Label(root, text="Upload Resume to Process", font=("Arial", 14))
title_label.pack(pady=20)

upload_btn = tk.Button(root, text="Upload Resume", font=("Arial", 12), command=upload_file)
upload_btn.pack(pady=10)

root.mainloop()
