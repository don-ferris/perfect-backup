import hashlib
import tarfile
import os
import time
import shutil
import sys

source_dir = sys.argv[1]
backup_file = sys.argv[2]

current_time = time.strftime("%Y-%m-%d-%H%M", time.gmtime())
extract_dir = "/tmp/" + current_time

if len(sys.argv) != 3:
    print("Error: incorrect number of parameters. Usage: verify.py source_dir backup_file")
    sys.exit(1)

if not os.path.exists(backup_file):
    print("Error: backup file", backup_file, "does not exist")
    sys.exit(1)

if not tarfile.is_tarfile(backup_file):
    print("Error:", backup_file, "is not a tar archive")
    sys.exit(1)

if not os.path.exists(source_dir):
    print("Error: source directory", source_dir, "does not exist")
    sys.exit(1)

tar = tarfile.open(backup_file)
with tarfile.open(tar, "r:gz") as tarfilecount
    members = tar.getmembers()
    num_files = len(members) - 2
if len(tar.getnames()) != num_files:
    print("Error: the number of files in the tar archive and the source directory do not match")
    sys.exit(1)
tar.close()

# Create the extract_dir directory if it does not exist
if not os.path.exists(extract_dir):
    os.makedirs(extract_dir)

# Open the tar archive for reading
with tarfile.open(backup_file, 'r') as tar:

    # Keep track of whether there are any checksum errors
    error = False

    # Iterate through all the files in the tar archive
    for member in tar.getmembers():
        # Extract the file from the tar archive to the extract_dir directory
        tar.extract(member, extract_dir)

        # Calculate the MD5 checksum of the file in the tar archive
        with open(os.path.join(extract_dir, member.name), 'rb') as f:
            backup_checksum = hashlib.md5(f.read()).hexdigest()

        # Calculate the MD5 checksum of the corresponding source file
        with open(os.path.join(source_dir, member.name), 'rb') as f:
            source_checksum = hashlib.md5(f.read()).hexdigest()

        # Compare the checksums
        if backup_checksum != source_checksum:
            print(f'ERROR: Checksum mismatch for file {member.name}')
        else:
            # Delete the extracted file after the comparison is done
            os.remove(os.path.join(extract_dir, member.name))

    # Return a message if there are no checksum errors
    if not error:
        print('All files match their source counterparts.')

# Remove the extract_dir directory after all files have been processed
shutil.rmtree(extract_dir)

# close the tar archive
tar.close()
