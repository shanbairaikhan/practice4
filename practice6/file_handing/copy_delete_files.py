import shutil
import os



shutil.copy("file1.txt", "file1_copy.txt")




shutil.copy("file2.txt", "backup_file2.txt")



if os.path.exists("file1_copy.txt"):
    os.remove("file1_copy.txt")




shutil.copy("file3.txt", "copy3.txt")




if os.path.exists("copy3.txt"):
    os.remove("copy3.txt")




shutil.copy("data.txt", "data_backup.txt")




if os.path.exists("data_backup.txt"):
    print("Backup created")




if os.path.exists("data_backup.txt"):
    os.remove("data_backup.txt")




if os.path.exists("notes_copy.txt"):
    print("Copy exists")





if os.path.exists("notes_copy.txt"):
    os.remove("notes_copy.txt")





shutil.copy("text.txt", "text_copy.txt")




if os.path.exists("data1_copy.txt"):
    os.remove("data1_copy.txt")