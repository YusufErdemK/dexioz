#!/usr/bin/env python3
# dexioz.py
#sign of Erdamn
import os
import sys
import json
from organizer.organizer import organize_files, undo_organize
sys.path.append("/home/erdem/dexioz")

BACKUP_FILE = ".dexioz_backup.json"

def save_backup(folder, file_map):
    with open(os.path.join(folder, BACKUP_FILE), "w") as f:
        json.dump(file_map, f)

if __name__ == "__main__":
    target_folder = os.getcwd()

    if len(sys.argv) > 1 and sys.argv[1] == "-undo":
        undo_organize(target_folder, BACKUP_FILE)
    else:
        file_map = organize_files(target_folder, save_map=True)
        save_backup(target_folder, file_map)
