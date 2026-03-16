import os
import shutil

shutil.copy("file.txt", "folder1/file.txt")


shutil.move("file.txt", "folder1/file.txt")


shutil.copy("a.txt", "b.txt")


shutil.move("a.txt", "folder2/a.txt")


shutil.copy("data.txt", "backup/data.txt")


shutil.move("test.txt", "a/test.txt")


print(os.listdir())


print(os.listdir("folder1"))


shutil.copy("info.txt", "copy_info.txt")


shutil.move("copy_info.txt", "folder1/copy_info.txt")
