import os
import shutil
import math

def organize_reports():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Get all files in the current directory
    all_files = [f for f in os.listdir(base_dir) if os.path.isfile(os.path.join(base_dir, f))]
    
    # Filter out this script itself
    script_name = os.path.basename(__file__)
    if script_name in all_files:
        all_files.remove(script_name)
    
    # Sort files to ensure deterministic order (optional)
    all_files.sort()
    
    if not all_files:
        print("No files found to organize.")
        return

    files_per_person = 3
    num_people = math.ceil(len(all_files) / files_per_person)
    
    print(f"Found {len(all_files)} files.")
    print(f"Organizing into {num_people} folders (up to {files_per_person} files each).")

    for i in range(num_people):
        person_dir_name = f"{i + 1}. kişi"
        person_dir_path = os.path.join(base_dir, person_dir_name)
        
        if not os.path.exists(person_dir_path):
            os.makedirs(person_dir_path)
            print(f"Created directory: {person_dir_name}")
        
        # Determine which files go into this folder
        start_index = i * files_per_person
        end_index = start_index + files_per_person
        files_to_move = all_files[start_index:end_index]
        
        for filename in files_to_move:
            src_path = os.path.join(base_dir, filename)
            dst_path = os.path.join(person_dir_path, filename)
            try:
                shutil.move(src_path, dst_path)
                print(f"Moved {filename} to {person_dir_name}")
            except Exception as e:
                print(f"Error moving {filename}: {e}")

if __name__ == "__main__":
    organize_reports()
