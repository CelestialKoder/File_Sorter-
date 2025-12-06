import os       #these 2 lines important modules
import shutil
folder = os.getcwd()    #this will give location of parent dir
for files in os.listdir():
    location = os.path.join(folder,files)
    if os.path.isdir(location):    #this will check if the files in dir are really files or another dir
        continue
    if files == "file_sorter.exe":         #prevent the movement of exe file 
        continue
    name, ext = os.path.splitext(files)
    ext=ext.lower()                                #defining extension
    if ext in (".jpg",".jpeg",".png"):             #creating dir for images and locating it into the same folder
        try:
            os.makedirs(os.path.join(folder, "Images"))
        except FileExistsError:
            pass
        shutil.move(location,os.path.join(folder, "Images"))
    elif ext in (".pdf", ".docx"):          #creating dir for images and locating it into the same folder
        try:
            os.makedirs(os.path.join(folder, "Documents"))
        except FileExistsError:
            pass
        shutil.move(location,os.path.join(folder, "Documents"))

    else:
        try:                            #creating dir for images and locating it into the same folder
            os.makedirs(os.path.join(folder, "Other"))
        except FileExistsError:
            pass
        shutil.move(location,os.path.join(folder, "Other"))
    
    