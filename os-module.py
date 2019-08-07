import os
from datetime import datetime

# print(dir(os))
# print(os.getcwd())

# os.chdir("C://")
# print(os.getcwd())

# os.mkdir("OS-Demo-2\Sub-Dir-1")
# os.makedirs("OS-Demo-2\Sub-Dir-1")

# os.rmdir("OS-Demo-2")
# os.removedirs("OS-Demo-2\Sub-Dir-1")  # recursive delete

# mod_time = os.stat("Intro.py").st_mtime
# print(datetime.fromtimestamp(mod_time))

# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     print("Current Path:", dirpath)
#     print("Current names:", dirnames)
#     print("Current filenames:", filenames)
#     print()
# print(os.listdir())

# print(os.environ)
# print(os.environ.get("HOMEPATH"))
file_path = os.path.join(os.environ.get("HOMEPATH"), "test.txt")
# print(file_path)

print(os.path.dirname("/tmp/test.txt"))
print(os.path.split("/tmp/test.txt"))
print(os.path.exists("/tmp/test.txt"))
print(os.path.isdir("/tmp"))
print(os.path.isfile("/tmp/test.txt"))
print(os.path.splitext("/tmp/test.txt"))

