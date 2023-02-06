import sys
import tarfile
import os
import shutil
import time

if len(sys.argv) < 2:
    directory = os.getcwd()
    confirm = input("No directory specified. Backup current directory '{}'? (y/n) ".format(directory))
    if confirm != 'y':
        sys.exit()
else:
    directory = sys.argv[1]

if not os.path.exists(directory):
    print("Error: directory '{}' does not exist".format(directory))
    sys.exit()

if not os.listdir(directory):
    print("Error: directory '{}' is empty".format(directory))
    sys.exit()

backup_source = directory.replace("/", "-")

current_time = time.strftime("%Y-%m-%d-%H%M", time.gmtime())
backup_file = "BACKUP" + backup_source + "-" + current_time + ".tar.gz"

with tarfile.open(backup_file, "w:gz") as tar:
    tar.add(directory, arcname=os.path.basename(directory), recursive=True)

shutil.copystat(directory, backup_file)

print("Backup created: ", backup_file)
