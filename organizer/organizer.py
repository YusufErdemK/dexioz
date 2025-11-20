# organizer/organizer.py
# sign of Erdamn

import json
import os
import shutil
from filetypes import get_category

def organize_files(target_folder, save_map=False):
    file_map = {}
    for item in os.listdir(target_folder):
        item_path = os.path.join(target_folder, item)
        if os.path.isfile(item_path):
            ext = item.split(".")[-1]
            category = get_category(ext)
            category_folder = os.path.join(target_folder, category)
            
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)
            
            new_path = os.path.join(category_folder, item)
            if save_map:
                file_map[new_path] = item_path
            shutil.move(item_path, new_path)
    print("Files have been organized! ✅")
    return file_map

def undo_organize(target_folder, backup_file):
    backup_path = os.path.join(target_folder, backup_file)
    if not os.path.exists(backup_path):
        print("Backup for undo not found! ❌")
        return

    with open(backup_path, "r") as f:
        file_map = json.load(f)
    
    for new_path, old_path in file_map.items():
        if os.path.exists(new_path):
            shutil.move(new_path, old_path)
    os.remove(backup_path)
    print("Files have been restored to their previous state! 🔄")
    