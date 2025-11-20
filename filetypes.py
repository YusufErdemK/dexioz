# filetypes.py
# sign of Erdamn

FILE_TYPES = {
    "images": ["jpg", "jpeg", "png", "gif", "bmp", "svg"],
    "videos": ["mp4", "mkv", "mov", "avi"],
    "documents": ["pdf", "docx", "txt", "xlsx", "pptx"],
    "audio": ["mp3", "wav", "flac", "ogg"],
    "archives": ["zip", "rar", "tar", "gz"]
}

def get_category(file_extension):
    file_extension = file_extension.lower()
    for category, extensions in FILE_TYPES.items():
        if file_extension in extensions:
            return category
    return "others"
