import os
import shutil
import json
import threading

from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk


#Helper functions
def show_info(title, message):
    root.after(0, lambda: messagebox.showinfo(title, message))

def show_error(title, message):
    root.after(0, lambda: messagebox.showerror(title, message))

#for multithreading
def organize_files_thread():
    threading.Thread(target=organize_files, daemon=True).start()

#main function to move files
def organize_files():
    root.after(0, lambda: progress.config(value=0))
    try:
        # always look for config.json next to this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, "config.json")

        with open(config_path, "r") as f:
            rules = json.load(f)

        downloads_folder_location = os.path.join(os.path.expanduser("~"), "Downloads")

        files_in_downloads_folder = os.listdir(downloads_folder_location)

        if not files_in_downloads_folder:
            show_info("Info", "No items in Downloads.")
            return

        moved_count = 0

        #set progress bar value
        progress["value"] = 0
        progress["maximum"] = len(files_in_downloads_folder)

        for filename in files_in_downloads_folder:
            full_path_of_file = os.path.join(downloads_folder_location, filename)

            if os.path.isdir(full_path_of_file):  #skip directories
                continue

            ext = filename.split(".")[-1].lower() if "." in filename else ""
            if ext in rules:
                folder_name = rules[ext]
            else:
                folder_name = "Others"

            target_folder = os.path.join(downloads_folder_location, folder_name)
            destination_file_path = os.path.join(target_folder, filename)
            os.makedirs(target_folder, exist_ok=True)

            shutil.move(full_path_of_file, destination_file_path)
            moved_count += 1
            root.after(0, lambda count=moved_count: progress.config(value=count)) #progress bar proceeds based on moved_count

        show_info("Success", f"Organized {moved_count} files.")

    except PermissionError as e:
        show_error('Error', f"Insufficient permissions, try running as administrator.\n{e}")
    except FileNotFoundError as e:
        show_error("Error", f"config.json not found.\n{e}")
    except Exception as e:
        show_error("Error", str(e))
    



# --- Tkinter UI ---
root = tk.Tk()
root.title("File Organizer")

button = tk.Button(root, text="Organize files", command=organize_files_thread) 
button.pack(padx=40, pady=40)

progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress.pack(pady=10)

window_width = 500
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.mainloop()
