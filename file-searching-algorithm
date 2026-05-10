def read_file(path): 
    parts = path.split(".")
    file_type = parts[1] if len (parts) > 1 else "file"

    try: 
        with open(path, "r", encoding="utf-8") as f: 
            return f.read()
        except FileNotFoundError: 
            return file_type + " not found"
