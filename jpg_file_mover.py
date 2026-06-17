# ============================================================
#  TASK 3 — Task Automation with Python Scripts
#  CodeAlpha Python Programming Internship
#  Script: Automatically move all .jpg files to a new folder
#  Author: Saurabh Singh Tanwar
#  Date  : June 2025
# ============================================================

# os module — used for file/folder operations
# (checking existence, listing files, creating directories, building paths)
import os

# shutil module — used for moving and copying files
# (works like Cut + Paste on your computer, but through code)
import shutil


# ============================================================
# FUNCTION 1 — Get source and destination folder paths
# ============================================================
def get_folders():
    """
    Prompt the user to enter the source and destination folder paths.
    Source      = folder where .jpg files currently exist
    Destination = folder where .jpg files will be moved to
    """

    print("\n" + "=" * 50)
    print("   📁  JPG FILE MOVER — CodeAlpha Task 3")
    print("=" * 50)

    # Ask user for the source folder path
    print("\n📂 SOURCE FOLDER")
    print("   (The folder that contains your .jpg files)")
    print("   Example: C:\\Users\\Saurabh\\Pictures")
    print("   Press Enter to use the current folder\n")

    source = input("   Enter source folder path: ").strip()

    # If the user pressed Enter without typing anything,
    # use the current working directory as the source
    if source == "":
        source = os.getcwd()   # getcwd = Get Current Working Directory
        print(f"   ✅ Using current folder: {source}")

    # Ask user for the destination folder path
    print("\n📁 DESTINATION FOLDER")
    print("   (The folder where .jpg files will be moved)")
    print("   Example: C:\\Users\\Saurabh\\JPG_Files")
    print("   Press Enter to create a 'JPG_Files' folder automatically\n")

    destination = input("   Enter destination folder path: ").strip()

    # If the user pressed Enter without typing anything,
    # create a default 'JPG_Files' folder inside the source folder
    if destination == "":
        destination = os.path.join(source, "JPG_Files")
        print(f"   ✅ Default destination: {destination}")

    return source, destination


# ============================================================
# FUNCTION 2 — Verify that the source folder exists
# ============================================================
def check_source_folder(source):
    """
    Check whether the given source folder path actually exists.
    Returns True if valid, False if not found.
    """

    # os.path.exists() returns True if the path exists, False otherwise
    if not os.path.exists(source):
        print(f"\n❌ ERROR: Source folder not found!")
        print(f"   Path : {source}")
        print(f"   Please double-check the folder path and try again.\n")
        return False   # Signal that something went wrong

    return True        # Signal that everything is fine


# ============================================================
# FUNCTION 3 — Create the destination folder if it doesn't exist
# ============================================================
def create_destination_folder(destination):
    """
    Create the destination folder if it does not already exist.
    """

    # Check if the destination folder already exists
    if not os.path.exists(destination):

        # os.makedirs() creates the folder (and any parent folders if needed)
        os.makedirs(destination)
        print(f"\n✅ New folder created: {destination}")

    else:
        print(f"\n✅ Destination folder already exists: {destination}")


# ============================================================
# FUNCTION 4 — Scan and move all .jpg files
# ============================================================
def move_jpg_files(source, destination):
    """
    Scan the source folder for all .jpg files and move them
    to the destination folder.
    Returns three lists: moved, skipped, and error files.
    """

    moved_files   = []   # Files successfully moved
    skipped_files = []   # Files skipped due to duplicate names
    error_files   = []   # Files that encountered an error

    print(f"\n🔍 Scanning folder: {source}")
    print("-" * 50)

    # os.listdir() returns a list of all files and folders in the directory
    all_files = os.listdir(source)

    # Iterate through each file in the source folder
    for file_name in all_files:

        # .lower() converts the filename to lowercase
        # so that both ".jpg" and ".JPG" are detected correctly
        # .endswith() checks if the filename ends with ".jpg"
        if file_name.lower().endswith(".jpg"):

            # Build the full path for the source file
            # os.path.join() safely combines folder path + filename
            source_path      = os.path.join(source, file_name)

            # Build the full path for the destination file
            destination_path = os.path.join(destination, file_name)

            # Check if a file with the same name already exists
            # in the destination folder to avoid overwriting
            if os.path.exists(destination_path):
                print(f"   ⚠️  SKIPPED (already exists): {file_name}")
                skipped_files.append(file_name)
                continue   # Skip this file and move to the next one

            # Attempt to move the file using shutil.move()
            # try-except ensures the program doesn't crash on errors
            try:
                # shutil.move() moves the file from source to destination
                shutil.move(source_path, destination_path)
                print(f"   ✅ MOVED: {file_name}")
                moved_files.append(file_name)

            except Exception as error:
                # Catch any unexpected error and log it
                print(f"   ❌ ERROR moving {file_name}: {error}")
                error_files.append(file_name)

    return moved_files, skipped_files, error_files


# ============================================================
# FUNCTION 5 — Display final summary
# ============================================================
def print_summary(moved_files, skipped_files, error_files, destination):
    """
    Display a clean summary of the operation results.
    """

    print("\n" + "=" * 50)
    print("   📊  SUMMARY")
    print("=" * 50)

    print(f"\n   ✅  Successfully moved  : {len(moved_files)} file(s)")
    print(f"   ⚠️   Skipped (duplicate) : {len(skipped_files)} file(s)")
    print(f"   ❌  Errors              : {len(error_files)} file(s)")

    # If files were moved, list their names
    if moved_files:
        print(f"\n   📁  Moved to: {destination}")
        print("   Files moved:")
        for file in moved_files:
            print(f"      → {file}")

    # If no .jpg files were found at all
    if len(moved_files) == 0 and len(skipped_files) == 0:
        print("\n   ℹ️  No .jpg files found in the source folder.")
        print("      Please add some .jpg files and try again.")

    print("\n" + "=" * 50 + "\n")


# ============================================================
# MAIN FUNCTION — Entry point of the script
# ============================================================
def main():
    """
    Main function — orchestrates all steps in sequence:
    1. Get folder paths from user
    2. Validate source folder
    3. Create destination folder
    4. Move .jpg files
    5. Display summary
    """

    # Step 1 — Get source and destination folder paths from the user
    source, destination = get_folders()

    # Step 2 — Verify that the source folder exists
    # If it doesn't, stop execution immediately
    if not check_source_folder(source):
        return

    # Step 3 — Create the destination folder if it doesn't already exist
    create_destination_folder(destination)

    # Step 4 — Scan for .jpg files and move them
    moved, skipped, errors = move_jpg_files(source, destination)

    # Step 5 — Display the final result summary
    print_summary(moved, skipped, errors, destination)


# ============================================================
# Entry Point
# This block ensures main() only runs when this file is
# executed directly — not when imported as a module
# ============================================================
if __name__ == "__main__":
    main()
