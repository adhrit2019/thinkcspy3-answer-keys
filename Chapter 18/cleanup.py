import os

def clean_files(path="."):
    files = os.listdir(path)
    files.sort()

    for file in files:
        fullname = os.path.join(path, file)
        if file == "trash.txt":
            os.remove(fullname)
        elif os.path.isdir(fullname):
            clean_files(fullname)

clean_files("/home/adhrit/Documents/python_exer/github_projects/thinkcspy3-answer-keys/Chapter 18/examples")

