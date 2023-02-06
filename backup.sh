#!/bin/bash

# Get the source directory
src_dir=$1
# or hard code it into the script
# src_dir="/home/user"

# Check if the source directory exists
if [ ! -d "$src_dir" ]; then
  echo "Error: $src_dir is not a valid directory"
  exit 1
fi

# Get the machine name, user name, and current date
machine_name=$(hostname)
user_name=$(whoami)
current_date=$(date +"%Y-%m-%d")

# Set the target archive file name
target_file="${machine_name}_${user_name}_${current_date}.tar.gz"

# Backup the files in the source directory with their permissions and UID/GID tags
tar czvf "$target_file" --preserve-permissions --same-owner "$src_dir"

# Verify the backup was created successfully
if [ $? -eq 0 ]; then
  echo "Backup completed successfully"
else
  echo "Backup failed"
fi
