from os import path
import re

def Open(file_name, mode):
    
    current_dir = path.dirname(__file__)
    file_path = path.join(current_dir,file_name)
    
    try:
        file = open(file_path, mode)
    except:
        print(f"File {file_name} wasn't opened!")
        return None
    else:
        print(f"File {file_name} was opened!")
        return file

file1_name = "TF1_1.txt"
file2_name = "TF1_2.txt"

file1_w = Open(file1_name, "w")
if file1_w != None:
    
    file1_w.write("Happiness is not by chance, but by choice\n")
    file1_w.write("Sometimes you win, sometimes you learn.")
    
    print("Information was successfully added to "+file1_name)
    
    file1_w.close()
    print(f"File {file1_name} was closed!")

file1_r = Open(file1_name, "r")
file2_w = Open(file2_name, "w")

if file1_r != None and file2_w != None:
    
    for block in file1_r.read().split("\n"):
            
        block = re.sub(r"\!|\?|\.|\,|\-|\:", " ", block).strip()
        
        for word in block.strip().split():
            file2_w.write(word+"\n")
            
    print("Information was successfully added to " + file2_name)
    
    file1_r.close()
    print(f"File {file1_name} was closed!")
    file2_w.close()
    print(f"File {file2_name} was closed!")

file2_r = Open(file2_name, "r")
if file2_r != None:
    
    print(f"Words from file {file1_name} :")
    for block in file2_r.read().split():
        print(block.strip())
    
    file2_r.close()
    print(f"File {file2_name} was closed!")