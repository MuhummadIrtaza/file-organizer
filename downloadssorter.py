import os  
import pathlib 
path = "/home/irtaza/Downloads"
files = [f for f in os.listdir(path)]
images= [".jpg" , ".png"]


def make_folders():
        os.makedirs(path + "/images")
        os.makedirs(path + "/executables")
        os.makedirs(path + "/miscallaneous")
        os.makedirs(path + "/music")

for items in files:
    try:
        extention = pathlib.Path(items).suffix
        print(extention)

    except:
        print("lol")


make_folders()
