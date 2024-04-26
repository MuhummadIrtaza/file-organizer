import os  
import pathlib 
import shutil

path = input("Enter the path you want to organize the files: ")
files = [f for f in os.listdir(path)]


def make_folders():
    file_paths = ["/images" , "/executables" , "/miscallaneous" , "/music" , "/videos" , "/books" , "/compressed"]                                                                                                                                                                                                                                          

    for paths in file_paths:
        if not os.path.exists(path + paths):
            os.makedirs(path + paths)

def sort():

    imgs = [".jpg", ".png", ".gif", ".bmp", ".tiff"]
    execs = [".exe", ".com", ".bat", ".msi", "..app"]
    videos = [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".mpeg", ".m4v", ".webm", ".rmvb"]
    music = [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".ape", ".alac", ".midi"]
    books = [".pdf" , ".epub"]
    compressed = [".zip", ".rar", ".7z", ".tar", ".gzip", ".bz2", ".xz", ".tar.gz", ".tar.bz2", ".tar.xz", ".gz", ".bz2", ".xz"]

    for items in files:
        extensions = pathlib.Path(items).suffix
        src_path = path + "/" + items

        # move extensions of images to images file
        if extensions in imgs:
            dst_path = path + "/images"
            shutil.move(src_path , dst_path)
            
        #move extension of executables to executables file
        elif extensions in execs:
            dst_path = path + "/executables"
            shutil.move(src_path , dst_path)

        #move music files
        elif extensions in music:
            dst_path = path + "/music"
            shutil.move(src_path , dst_path)

        #move compressed files
        elif extensions in compressed:
            dst_path = path + "/compressed"
            shutil.move(src_path , dst_path)

        elif extensions in books:
            dst_path = path + "/books"
            shutil.move(src_path , dst_path)

        #move miscallaneous
        else:
            dst_path  = path + "/miscallaneous"
            if not os.path.exists(os.path.join(dst_path, items)):
                shutil.move(src_path, dst_path)





if __name__ == "__main__":
    make_folders()
    sort()
