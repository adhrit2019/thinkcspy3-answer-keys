import os

def make_litter(path):
    files = os.listdir(path)
    files.sort()
    for directory in files:
        fullname = "/".join([path, directory])
        if os.path.isdir(fullname):
            f = open(os.path.join(fullname, "trash.txt"), "w")
            f.close()
            make_litter(fullname)


make_litter("/home/adhrit/Documents/python_exer/github_projects/thinkcspy3-answer-keys/Chapter 18/examples")
