# File Organizer – Automatically sort your directory of choice

A simple GUI application that automatically organizes files in your chosen directory based on configurable file extension rules.

<img width="495" height="327" alt="image" src="https://github.com/user-attachments/assets/af9f142f-6988-4944-b712-8b636c4ec06a" />

<img width="498" height="330" alt="image" src="https://github.com/user-attachments/assets/31d959bc-c22f-4a4e-bfb7-a0893e841993" />

---

## ⚠️ Warning:
It is highly recommended to choose one or two target folders at most.
The program creates subfolders based on file extensions in the target directory.
If you run multiple batches with the same extensions in different target folders, files with the same type may end up in different subfolders, which can make organization confusing.

## Features

- **Automatic File Organization**: Sorts files from your chosen directory in categorized subfolders into your target directory
- **Configurable Rules**: Uses a JSON configuration file to define file extension mappings
- **User-Friendly GUI**: Clean tkinter interface with progress tracking
- **Threaded Operations**: Non-blocking file operations to maintain UI responsiveness
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Requirements

- Python 3.6+
- No external libraries required

## Installation

1. Clone the repository or download a standalone executable here: https://github.com/Allkindoflower/file-organizer/releases/tag/tool
2. Ensure Python 3.6+ is installed on your system
3. Create a `config.json` file in the same directory as the script

## Configuration

Create a `config.json` file in the same directory as the application with your file organization rules:

```json
{
  "pdf": "Documents",
  "doc": "Documents",
  "docx": "Documents",
  "txt": "Documents",
  "jpg": "Images",
  "jpeg": "Images",
  "png": "Images",
  "gif": "Images",
  "mp4": "Videos",
  "avi": "Videos",
  "mkv": "Videos",
  "mp3": "Audio",
  "wav": "Audio",
  "zip": "Archives",
  "rar": "Archives",
  "exe": "Programs",
  "msi": "Programs"
}
```

### Configuration Rules

- **Key**: File extension (without the dot)
- **Value**: Target folder name where files with this extension will be moved
- Files with extensions not listed in the configuration will be moved to an "Others" folder
- Folder names are case-sensitive and will be created as subfolders in your target directory

## Usage
0. It is highly recommended you click on How it works button once you have launched the program for a quick rundown.
  
1. Run the application:
   ```bash
   python file_organizer.py
   ```
...

skip this step if you have downloaded the program instead.

2. Click the "Organize Files" button to start the organization process

3. The progress bar will show the current operation status

4. A success message will display the number of files organized

## How It Works

The application scans your source folder, identifies file extensions, and moves files to the corresponding subfolders defined in config.json. Files not listed in the configuration are placed in an “Others” folder.

## Error Handling

The application handles common errors gracefully:

- **Permission Errors**: Displays a message suggesting to run as administrator
- **Missing Configuration**: Shows an error if `config.json` is not found
- **General Exceptions**: Catches and displays any unexpected errors

## File Structure

```
file-organizer/
├── file_organizer.exe    # Main application file
├── config.json          # Configuration file (user-created)
├── README.md
```

## Safety Notes

- Windows may flag the program as unsafe, you can safely disregard the notice.
- The application only moves files, it doesn't delete them
- Directories are skipped and left untouched
- Original file names and extensions are preserved

## Troubleshooting

### "config.json not found" Error
Ensure the `config.json` file is in the same directory as the Python script.

### Permission Errors
Try running the application with administrator privileges:
- **Windows**: Right-click and select "Run as administrator"
- **macOS/Linux**: Use `sudo python file_organizer.py`

### No Files Moved
Check that your source folder contains files (not just directories) and that your `config.json` is properly formatted.

## License

This project is open source and available under the MIT License.

## Additional Notes

If you have ideas, questions or bug reports for this project, I'm open to feedback. You can reach me at: bastugugur85@gmail.com

