import os
import shutil

downloads_folder_location = r"path-to-your-downloads-folder"
desktop_location_path = os.path.join(os.path.expanduser("~"), "Desktop")

extensions = {
    'pdf': 'PDFs',
    'png': 'Images',
    'jpg': 'Images',
    'gif': 'Images',
    'exe': 'Applications',
    'odt': 'Important docs',
    'docx': 'Important docs',
    'txt': 'Important docs',
    'zip': 'Zip files', 
}

files_in_downloads_folder = os.listdir(downloads_folder_location)

for filename in files_in_downloads_folder:
    full_path_of_file = os.path.join(downloads_folder_location, filename)#creates the full file location
    
    if os.path.isdir(full_path_of_file):#if selected thing is a folder or doesnt have an extension skip it
        continue

    ext = filename.split('.')[-1].lower()#gets the extension name
    if ext in extensions:
        folder_name = extensions[ext]
        target_folder = os.path.join(desktop_location_path, folder_name)

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        shutil.move(full_path_of_file, os.path.join(target_folder, filename))
        print(f"Moved {filename} to {folder_name}")

    else:
        target_folder = os.path.join(desktop_location_path, 'Others')
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        shutil.move(full_path_of_file, os.path.join(target_folder, filename))
        print(f"Moved {filename} to 'Others'")
input('press enter to continue ')
