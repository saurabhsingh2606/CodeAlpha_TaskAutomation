# 📁 Task Automation — JPG File Mover | CodeAlpha Internship Task 3

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Internship-CodeAlpha-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Task-3%20of%204-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Type-Automation%20Script-purple?style=for-the-badge" />
</p>

---

## 📌 About the Project

A **Python Automation Script** built as part of the **CodeAlpha Python Programming Internship**.

This script automatically scans a source folder, detects all `.jpg` files, and moves them into a designated destination folder — eliminating the need to manually sort through hundreds of image files.

---

## 🕹️ How It Works

```
1. Run the script
2. Enter the source folder path (where .jpg files are located)
3. Enter the destination folder path (where files should be moved)
4. Script scans the source folder automatically
5. All .jpg / .JPG files are moved to the destination
6. A detailed summary is displayed at the end
```

---

## 🖥️ Demo Preview

```
==================================================
   📁  JPG FILE MOVER — CodeAlpha Task 3
==================================================

📂 SOURCE FOLDER
   Enter source folder path: C:\Users\Saurabh\Pictures
   
📁 DESTINATION FOLDER
   Enter destination folder path:
   ✅ Default destination: C:\Users\Saurabh\Pictures\JPG_Files

✅ New folder created: C:\Users\Saurabh\Pictures\JPG_Files

🔍 Scanning folder: C:\Users\Saurabh\Pictures
--------------------------------------------------
   ✅ MOVED: holiday_photo.jpg
   ✅ MOVED: selfie.jpg
   ⚠️  SKIPPED (already exists): old_pic.jpg
   ✅ MOVED: college_event.jpg

==================================================
   📊  SUMMARY
==================================================
   ✅  Successfully moved  : 3 file(s)
   ⚠️   Skipped (duplicate) : 1 file(s)
   ❌  Errors              : 0 file(s)

   📁  Moved to: C:\Users\Saurabh\Pictures\JPG_Files
   Files moved:
      → holiday_photo.jpg
      → selfie.jpg
      → college_event.jpg
==================================================
```

---

## ✨ Features

- 📂 **Auto Folder Creation** — Destination folder is created automatically if it doesn't exist
- 🔍 **Case-Insensitive Detection** — Detects both `.jpg` and `.JPG` file extensions
- ⚠️ **Duplicate File Handling** — Skips files that already exist in the destination
- 📊 **Detailed Summary** — Shows count of moved, skipped, and failed files
- 🛡️ **Error Handling** — Uses `try-except` to prevent crashes on unexpected errors
- ⌨️ **Default Path Support** — Press Enter to use smart default paths

---

## 📂 Project Structure

```
CodeAlpha_TaskAutomation/
│
├── jpg_file_mover.py    ← Main automation script
└── README.md            ← Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed → [Download here](https://python.org)
- No external libraries required — uses only built-in `os` and `shutil` modules!

### Run the Script

```bash
# Clone the repository
git clone https://github.com/saurabhsingh2606/CodeAlpha_TaskAutomation.git

# Navigate into the folder
cd CodeAlpha_TaskAutomation

# Run the script
python jpg_file_mover.py
```

---

## 🧠 Concepts & Technologies Used

| Concept | Usage in Project |
|---|---|
| `os` module | Scanning folders, checking paths, building file paths |
| `shutil` module | Moving files from source to destination |
| `os.listdir()` | Getting a list of all files in the source folder |
| `os.path.exists()` | Checking if a file or folder already exists |
| `os.makedirs()` | Creating the destination folder automatically |
| `os.path.join()` | Safely combining folder path + filename |
| `shutil.move()` | Physically moving a file (like Cut + Paste) |
| `try-except` | Handling unexpected errors gracefully |
| `.lower()` | Converting filename to lowercase for case-insensitive matching |
| `.endswith()` | Checking if a filename ends with `.jpg` |
| `list.append()` | Storing results in moved, skipped, and error lists |
| `f-strings` | Producing clean and formatted console output |

---

## 🔮 Future Improvements

- [ ] Support for multiple file types (`.png`, `.gif`, `.bmp`, `.webp`)
- [ ] Recursive scan — search inside subfolders as well
- [ ] GUI version using `tkinter`
- [ ] Generate a log file recording every move operation with timestamps
- [ ] Undo feature — move files back to their original location

---

## 👨‍💻 Author

**Saurabh Singh Tanwar**
🎓 BSc Computer Science — 5th Semester
🏫 Guru Ghasidas Vishwavidyalaya, Bilaspur, Chhattisgarh
🐙 [GitHub](https://github.com/saurabhsingh2606)

---

## 🏢 Internship

This project was built as **Task 3** of the **Python Programming Internship** at
**[CodeAlpha](https://www.codealpha.tech)** — A leading software development company.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ during CodeAlpha Python Internship
</p>
