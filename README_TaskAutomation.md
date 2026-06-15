# 📁 Task Automation — JPG File Mover | CodeAlpha Internship Task 2

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Internship-CodeAlpha-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Task-3%20of%204-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Type-Automation%20Script-purple?style=for-the-badge" />
</p>

---

## 📌 About the Project

A **Python Automation Script** built as part of the **CodeAlpha Python Programming Internship**.  
This script automatically finds all `.jpg` files in a source folder and moves them to a new destination folder — saving time and effort compared to doing it manually!

---

## 🕹️ How It Works

```
1. Run the script
2. Enter the SOURCE folder path (where .jpg files are)
3. Enter the DESTINATION folder path (where to move them)
4. Script scans the source folder automatically
5. All .jpg / .JPG files are moved to destination
6. A summary is displayed at the end
```

---

## 🖥️ Demo Preview

```
==================================================
   📁  JPG FILE MOVER — CodeAlpha Task 2
==================================================

📂 SOURCE FOLDER kahan hai?
   Source folder path: C:\Users\Saurabh\Pictures

📁 DESTINATION FOLDER kahan banana hai?
   Destination folder path:
   ✅ Default folder use hoga: C:\Users\Saurabh\Pictures\JPG_Files

✅ Naya folder banaya gaya: C:\Users\Saurabh\Pictures\JPG_Files

🔍 Scanning folder...
   ✅ MOVED: photo1.jpg
   ✅ MOVED: photo2.jpg
   ⚠️  SKIP (already exists): photo3.jpg

==================================================
   📊  SUMMARY
==================================================
   ✅  Successfully moved  : 2 files
   ⚠️   Skipped (duplicate) : 1 file
   ❌  Errors              : 0 files
==================================================
```

---

## ✨ Features

- 📂 **Auto Folder Creation** — Destination folder automatically ban jaata hai
- 🔍 **Smart Detection** — `.JPG` (capital) bhi detect karta hai, sirf `.jpg` nahi
- ⚠️ **Duplicate Handling** — Same naam ki file already hai toh skip kar deta hai
- 📊 **Clean Summary** — Moved / Skipped / Errors ka count dikhata hai
- 🛡️ **Error Handling** — try-except se unexpected errors ko handle karta hai

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
- No extra libraries needed — `os` and `shutil` Python ke saath already aate hain!

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

| Concept | Usage |
|---|---|
| `os` module | Folder scan karna, path banana, exist check karna |
| `shutil` module | Files move karna (cut-paste) |
| `os.listdir()` | Folder ke andar ki saari files ki list lena |
| `os.path.exists()` | File ya folder exist karta hai check karna |
| `os.makedirs()` | Naya folder banana |
| `os.path.join()` | Folder + filename = full path banana |
| `shutil.move()` | File ko source se destination pe move karna |
| `try-except` | Errors handle karna — program crash na ho |
| `list.append()` | Result lists mein file names store karna |
| `f-strings` | Clean formatted output dikhana |

---

## 🔮 Future Improvements

- [ ] Multiple file types support (`.png`, `.gif`, `.bmp`)
- [ ] Recursive search — subfolders mein bhi dhundhe
- [ ] GUI version using `tkinter`
- [ ] Log file banana — kab kya move hua record kare
- [ ] Undo feature — files wapas original jagah bhejo

---

## 👨‍💻 Author

**Saurabh Singh Tanwar**  
🎓 BSc Computer Science (5th Semester)  
🏫 Guru Ghasidas Vishwavidyalaya, Bilaspur, Chhattisgarh  
🐙 [GitHub](https://github.com/saurabhsingh2606)

---

## 🏢 Internship

This project was built as **Task 2** of the **Python Programming Internship** at  
**[CodeAlpha](https://www.codealpha.tech)** — A leading software development company.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ during CodeAlpha Python Internship
</p>
