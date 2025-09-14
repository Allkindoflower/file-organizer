import os
import shutil
import json
import threading

from tkinter import messagebox, filedialog
import tkinter as tk
import tkinter.ttk as ttk

# --- Helper functions ---
def show_info(title, message):
    root.after(0, lambda: messagebox.showinfo(title, message))

def show_error(title, message):
    root.after(0, lambda: messagebox.showerror(title, message))

def show_how_it_works():
    message = (
        "1. Select the source folder containing your files.\n"
        "2. Select a target folder where subfolders will be created.\n"
        "   (If no target is selected, subfolders will be created in the source folder.)\n"
        "3. Click 'Organize Files' to move files into appropriate subfolders.\n"
        "4. Subfolders are created based on file extensions.\n"
        "5. Files that could not be moved will be reported at the end."
    )
    messagebox.showinfo("How it works", message)

# ---Global variables---
selected_folder = None
selected_target_folder = None
failed_files = []

# --- Folder selection ---
def choose_folder():
    global selected_folder
    folder = filedialog.askdirectory(title="Select folder to organize")
    if folder:
        selected_folder = folder
        selected_folder_label.config(text=f"Source folder:\n{folder}")

def choose_target_folder_location():
    global selected_target_folder
    folder = filedialog.askdirectory(title="Select target folder for organized subfolders")
    if folder:
        selected_target_folder = folder
        selected_target_folder_label.config(text=f"Target folder:\n{folder}")

# --- Multithreading setup ---
def organize_files_thread():
    threading.Thread(target=organize_files, daemon=True).start()

# --- Main file organization ---
def organize_files():
    global selected_folder, selected_target_folder, failed_files
    failed_files = []

    if not selected_folder:
        show_info("Error", "No source folder selected.")
        return

    folder_to_organize = selected_folder
    base_folder = selected_target_folder if selected_target_folder else folder_to_organize

    root.after(0, lambda: progress.config(value=0))

    # Load config.json
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.json")

    try:
        with open(config_path, "r") as f:
            rules = json.load(f)
    except FileNotFoundError:
        show_error("Error", "config.json not found.")
        return
    except json.JSONDecodeError as e:
        show_error("Error", f"Malformed config.json file.\n{e}")
        return

    files_in_folder = os.listdir(folder_to_organize)
    if not files_in_folder:
        show_info("Info", "No items in source folder.")
        return

    moved_count = 0
    progress["value"] = 0
    progress["maximum"] = len(files_in_folder)

    for filename in files_in_folder:
        full_path = os.path.join(folder_to_organize, filename)
        if os.path.isdir(full_path):
            continue

        ext = filename.split(".")[-1].lower() if "." in filename else ""
        folder_name = rules.get(ext, "Others")

        target_folder = os.path.join(base_folder, folder_name)
        os.makedirs(target_folder, exist_ok=True)
        destination_path = os.path.join(target_folder, filename)

        try:
            shutil.move(full_path, destination_path)
        except Exception as e:
            failed_files.append((filename, str(e)))
            continue

        moved_count += 1
        root.after(0, lambda count=moved_count: progress.config(value=count))

    show_info("Success", f"Organized {moved_count} files.")

    if failed_files:
        error_text = "\n".join([f"{f}: {msg}" for f, msg in failed_files])
        show_error("Files Not Moved", f"Some files could not be moved:\n{error_text}")

# --- Tkinter UI ---
root = tk.Tk()
root.title("File Organizer")

window_width = 500
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(False, False)

# Frame for top folder selection buttons
top_frame = tk.Frame(root)
top_frame.pack(pady=15)

choose_folder_button = tk.Button(top_frame, text="Select Source Folder", width=20, height=2, command=choose_folder)
choose_folder_button.grid(row=0, column=0, padx=10)

choose_target_folder_button = tk.Button(top_frame, text="Select Target Folder", width=20, height=2, command=choose_target_folder_location)
choose_target_folder_button.grid(row=0, column=1, padx=10)

# Labels under buttons
selected_folder_label = tk.Label(root, text="No source folder selected", wraplength=460, justify="center")
selected_folder_label.pack(pady=5)

selected_target_folder_label = tk.Label(root, text="No target folder selected", wraplength=460, justify="center")
selected_target_folder_label.pack(pady=5)

# Progress bar
progress = ttk.Progressbar(root, orient="horizontal", length=460, mode="determinate")
progress.pack(pady=10)

how_it_works_button = tk.Button(root, text="How it works", command=show_how_it_works)
how_it_works_button.pack(pady=5)

# Organize button at bottom, centered
organize_button = tk.Button(root, text="Organize Files", width=25, height=2, command=organize_files_thread)
organize_button.pack(side="bottom", pady=20)

root.mainloop()
