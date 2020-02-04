import shutil
import os

dir = ["./MBFL","./SBFL"]
for cleandir in dir:
    shutil.rmtree(cleandir)
    os.makedirs(cleandir)