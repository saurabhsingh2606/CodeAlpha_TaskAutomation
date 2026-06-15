# ============================================================
#  TASK 3 — Task Automation with Python Scripts
#  CodeAlpha Python Programming Internship
#  Script: Move all .jpg files to a new folder
# ============================================================

# --- Import kiye hain 2 tools ---
import os      # os = Operating System se baat karne ka tool
               # (files, folders dhundhna, banana — sab iske through)

import shutil  # shutil = file ko move/copy karne ka tool
               # (jaise ctrl+x, ctrl+v karna — but code se!)


# ============================================================
# FUNCTION 1 — Folders set karo
# ============================================================
def get_folders():
    """
    User se source aur destination folder ka path lo.
    Source  = jahan .jpg files abhi hain
    Destination = jahan move karni hain
    """

    print("\n" + "=" * 50)
    print("   📁  JPG FILE MOVER — CodeAlpha Task 3")
    print("=" * 50)

    # User se source folder path maango
    print("\n📂 SOURCE FOLDER kahan hai?")
    print("   (Woh folder jahan .jpg files hain)")
    print("   Example: C:\\Users\\Saurabh\\Pictures")
    print("   Ya press Enter for current folder (jahaan script hai)\n")

    source = input("   Source folder path: ").strip()

    # Agar kuch nahi diya toh current folder use karo
    if source == "":
        source = os.getcwd()   # getcwd = Get Current Working Directory
        print(f"   ✅ Current folder use hoga: {source}")

    # User se destination folder path maango
    print("\n📁 DESTINATION FOLDER kahan banana hai?")
    print("   (Jahan .jpg files move hongi)")
    print("   Example: C:\\Users\\Saurabh\\JPG_Files")
    print("   Ya press Enter for 'JPG_Files' folder (automatically banega)\n")

    destination = input("   Destination folder path: ").strip()

    # Agar kuch nahi diya toh source ke andar 'JPG_Files' folder banao
    if destination == "":
        destination = os.path.join(source, "JPG_Files")
        print(f"   ✅ Default folder use hoga: {destination}")

    return source, destination


# ============================================================
# FUNCTION 2 — Source folder exist karti hai ya nahi check karo
# ============================================================
def check_source_folder(source):
    """
    Check karo ki source folder sach mein exist karti hai.
    Agar nahi toh error do aur band karo.
    """

    # os.path.exists() = check karta hai ki path exist karta hai ya nahi
    if not os.path.exists(source):
        print(f"\n❌ ERROR: Source folder nahi mili!")
        print(f"   Path: {source}")
        print(f"   Dobara check karo path sahi hai ya nahi.\n")
        return False   # False = kuch galat hai

    return True        # True = sab sahi hai


# ============================================================
# FUNCTION 3 — Destination folder banao (agar pehle se nahi hai)
# ============================================================
def create_destination_folder(destination):
    """
    Destination folder banao agar pehle se exist nahi karti.
    """

    # os.path.exists() = check karo folder pehle se hai ya nahi
    if not os.path.exists(destination):

        # os.makedirs() = naya folder banao
        os.makedirs(destination)
        print(f"\n✅ Naya folder banaya gaya: {destination}")

    else:
        print(f"\n✅ Folder pehle se exist karta hai: {destination}")


# ============================================================
# FUNCTION 4 — .jpg files dhundho aur move karo
# ============================================================
def move_jpg_files(source, destination):
    """
    Source folder mein saari .jpg files dhundho
    aur destination folder mein move karo.
    """

    moved_files   = []   # Successfully move hue files ki list
    skipped_files = []   # Jo files skip hui (duplicate naam)
    error_files   = []   # Jo files move nahi huiyin (koi error)

    print(f"\n🔍 Scanning folder: {source}")
    print("-" * 50)

    # os.listdir() = folder ke andar ki saari files ki list do
    all_files = os.listdir(source)

    # Ek ek file check karo
    for file_name in all_files:

        # .lower() = sabko lowercase karo taaki .JPG bhi .jpg ban jaye
        # .endswith() = check karo file ka naam .jpg se khatam hota hai ya nahi
        if file_name.lower().endswith(".jpg"):

            # Source file ka poora path banao
            # os.path.join() = folder + file_name = full path
            source_path      = os.path.join(source, file_name)

            # Destination file ka poora path banao
            destination_path = os.path.join(destination, file_name)

            # Check karo kya same naam ki file destination mein pehle se hai
            if os.path.exists(destination_path):
                print(f"   ⚠️  SKIP (already exists): {file_name}")
                skipped_files.append(file_name)
                continue   # Yeh file skip karo, agle par jao

            # File ko move karo!
            try:
                # shutil.move() = file ko source se destination pe move karo
                shutil.move(source_path, destination_path)
                print(f"   ✅ MOVED: {file_name}")
                moved_files.append(file_name)

            except Exception as error:
                # Koi bhi unexpected error aaye toh
                print(f"   ❌ ERROR moving {file_name}: {error}")
                error_files.append(file_name)

    return moved_files, skipped_files, error_files


# ============================================================
# FUNCTION 5 — Final Summary print karo
# ============================================================
def print_summary(moved_files, skipped_files, error_files, destination):
    """
    Kaam khatam hone ke baad ek clean summary dikhao.
    """

    print("\n" + "=" * 50)
    print("   📊  SUMMARY")
    print("=" * 50)

    print(f"\n   ✅  Successfully moved  : {len(moved_files)} files")
    print(f"   ⚠️   Skipped (duplicate) : {len(skipped_files)} files")
    print(f"   ❌  Errors              : {len(error_files)} files")

    # Agar koi file move hui toh unke naam bhi dikhao
    if moved_files:
        print(f"\n   📁  Files moved to: {destination}")
        print("   Moved files:")
        for file in moved_files:
            print(f"      → {file}")

    # Agar koi file nahi mili
    if len(moved_files) == 0 and len(skipped_files) == 0:
        print("\n   ℹ️  Source folder mein koi .jpg file nahi mili!")
        print("      Kuch .jpg files daalo aur dobara try karo.")

    print("\n" + "=" * 50 + "\n")


# ============================================================
# MAIN FUNCTION — Sab kuch yahan se chalta hai
# ============================================================
def main():

    # Step 1 — User se folders ka path lo
    source, destination = get_folders()

    # Step 2 — Source folder exist karti hai? Check karo
    if not check_source_folder(source):
        return   # Agar folder nahi hai toh band karo

    # Step 3 — Destination folder banao (agar pehle se nahi hai)
    create_destination_folder(destination)

    # Step 4 — .jpg files dhundho aur move karo
    moved, skipped, errors = move_jpg_files(source, destination)

    # Step 5 — Summary dikhao
    print_summary(moved, skipped, errors, destination)


# ============================================================
# Entry Point — Jab file run hoti hai tab main() call hota hai
# ============================================================
if __name__ == "__main__":
    main()
