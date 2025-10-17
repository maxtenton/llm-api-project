import os

def ReadFile(FileName = ""):
    with open(f"sample_inputs/{FileName}", "r", encoding="utf-8") as file:
        return file.read()

def WriteOutput(FileName = "", Content = ""):
    if(not os.path.exists("output")):
        os.makedirs("output")
    with open(f"output/{FileName}", "w", encoding="utf-8") as file:
        file.write(Content)