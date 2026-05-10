# python-it-scripting-basics
Overview: 
Each script focuses on a specific, realistic scenario: 

1. Read a file safely:
   - Opens a file using a with block
   - Handles missing files with FileNotFoundError
   - Extracts the file extension for clearer error messages

2. Validate user input:
   - Prompts the user for numbers
   - Converts them using int()
   - Catches ValueError for invalid input
  
3. Parse a JSON file:
   - Loads JSON using json.load()
   - Handles missing files
   - Handles missing dictionary keys
  
4. Safe division:
   - Performs a / b
   - Catches ZeroDivisionError
   - Returns a clean, readable message
  
Included Functions: 

1. read_file(path):
   Reads a file and returns its contents.
   If the file doesn't exist, returns "filetype not found".

2. get_number():
   Prompts the user for a number and returns it as an integer.
   If conversion fails, returns "invalid number".

3. json_path(path):
   Loads a JSON file and returns a user-specified key.
   Handles both files and keys missing.

4. division(a, b):
   Divides two numbers safely.
   Returns "undefined division" if dividing by zero.

Technologies used: 
- Python 3.9.6
- Standard library only (json, file I/O, exceptions)
- No external dependencies

Purpose of this repository: 
This repository demonstrates: 

- Clean Python structure
- Real exception handling
- Defensive programming
- Practical IT scripting patterns
- Readable, maintainable code

It serves as a small but solid foundation for: 
- Automation scripts
- Log processors
- configuration readers
- Input driven utilities
- Junior IT portfolio projects

How to Run: 
1. Clone the repository:
   
   git clone <your-repo-url>
   cd <repo-name>

2. Run any script:

   python3 script_name.py

Background: 
These exercises were written to practice real Python, beyond what is typically taught in introductory university courses. They focus on the practical skills needed in IT environments: 

- Handling unexpected input
- Preventing crashes
- Writing robust functions
- Working with real files
- Parsing structured data
   



   
