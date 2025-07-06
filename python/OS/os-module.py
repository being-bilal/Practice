import os
from datetime import datetime

# to change current directory
os.chdir("/home/mmohdbilal/bilal/")
# creates directory
# os.makedirs("oss/demo")
# renames the directory
os.rename("test.py", "test2")
os.rename("test2", "test.py")
# deletes directory
os.removedirs("oss/demo")
# to get current directory
print(os.getcwd())
# list files stored in the directory
print(os.listdir())
# show file info
t = os.stat("test.py").st_mtime
m = datetime.fromtimestamp(t)
s = os.stat("test.py").st_size

print(f"last modidified on : {m}, size : {s}")
# to see entire directory tree and files within
for dirpath, dirname, file in os.walk("/home/mmohdbilal/bilal/test.py"):
    print("path : ", dirpath)
    print("directory : ", dirname)
    print("file name : ", file)
    print(" ")
# to get the directory location
print(os.environ.get("HOME"))

# os.path
# to join file with a path
print(os.path.join("/home/mmohdbilal/bilal", "test.py"))
# shows whether a file exists or not
print(os.path.exists("test.py"))
# grabs the file from the path
print(os.path.basename("/home/mmohdbilal/bilal/test.py"))
# grabs the directory from the path
print(os.path.dirname("/home/mmohdbilal/bilal/test.py"))
# return a absolute path
print(os.path.abspath("/home/mmohdbilal/bilal/test.py"))
# normalize the path by removing extra slashes
print(os.path.normpath("/home/mmohdbilal///bilal////test.py"))
# shows the size
print(os.path.getsize("/home/mmohdbilal/bilal/test.py"))
# splites the file and the path
print(os.path.split("/home/mmohdbilal/bilal/test.py"))
# splites the file, path, and extension
print(os.path.splitext("/home/mmohdbilal/bilal/test.py"))
