import json

def json_path(path): 
    key = input("enter a dictionary key: ")

    try: 
        with open(path, "r", encoding="utf-8") as f: 
            data = json.load(f)
        return data[key]
    except FileNotFoundError: 
        return "file not found"
    except KeyError: 
        return "key not found"
  
