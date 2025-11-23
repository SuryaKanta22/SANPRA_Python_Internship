import pathlib
import shutil
import sys

def organize_files(source_dir):
    """
    Organizes files in the source_dir into subfolders based on extensions.
    """
    source_path = pathlib.Path(source_dir)
    
    if not source_path.exists():
        print(f"Error: The directory '{source_dir}' does not exist.")
        return
    if not source_path.is_dir():
        print(f"Error: '{source_dir}' is not a directory.")
        return

    # Extension mapping
    extension_map = {
        '.pdf': 'Reports',
        '.csv': 'Data',
        '.xlsx': 'Data',
        '.xls': 'Data',
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.png': 'Images',
        '.gif': 'Images',
        '.txt': 'Text',
        '.docx': 'Documents',
        '.doc': 'Documents',
        '.pptx': 'Presentations',
        '.ppt': 'Presentations',
        '.mp3': 'Audio',
        '.wav': 'Audio',
        '.mp4': 'Video',
        '.mov': 'Video',
        '.zip': 'Archives',
        '.rar': 'Archives',
        '.py': 'Scripts',
        '.exe': 'Executables'
    }

    print(f"Scanning '{source_dir}'...")
    
    files_moved = 0
    
    for file_path in source_path.iterdir():
        if file_path.is_file():
            # Skip the script itself if it's in the same directory
            if file_path.name == pathlib.Path(__file__).name:
                continue
                
            file_extension = file_path.suffix.lower()
            
            # Determine folder name
            folder_name = extension_map.get(file_extension, 'Others')
            
            # Create destination folder path
            dest_folder = source_path / folder_name
            
            try:
                # Create directory if it doesn't exist
                dest_folder.mkdir(exist_ok=True)
                
                # Define destination file path
                dest_file = dest_folder / file_path.name
                
                # Handle duplicate filenames
                if dest_file.exists():
                    timestamp = pathlib.Path(file_path.stat().st_mtime).as_posix() # simplistic uniqueifier
                    dest_file = dest_folder / f"{file_path.stem}_{int(file_path.stat().st_mtime)}{file_path.suffix}"

                # Move the file
                shutil.move(str(file_path), str(dest_file))
                print(f"Moved: {file_path.name} -> {folder_name}/")
                files_moved += 1
                
            except Exception as e:
                print(f"Error moving {file_path.name}: {e}")

    print(f"\nOrganization complete. Moved {files_moved} files.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        source_directory = sys.argv[1]
    else:
        # Default to current directory if no argument provided, or ask user
        print("No directory specified.")
        source_directory = input("Enter the path of the folder to organize: ").strip()
        # Remove quotes if user added them
        if (source_directory.startswith('"') and source_directory.endswith('"')) or \
           (source_directory.startswith("'") and source_directory.endswith("'")):
            source_directory = source_directory[1:-1]

    if source_directory:
        organize_files(source_directory)
    else:
        print("No directory provided. Exiting.")
