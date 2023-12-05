#!/bin/bash

# Define source and destination directories
src_dir="/var/log"
dest_dir="~/backups"  # Using a relative path

# Ensure the destination directory exists, create it if necessary
mkdir -p "$dest_dir"

# Define source and destination filenames with timestamps
current=$(date +"%Y-%m-%d-%H:%M:%S")
src_file="$src_dir/syslog"
dest_file="$dest_dir/syslog-$current"

# Copy syslog file to the destination directory with timestamp
cp "$src_file" "$dest_file"

echo "Log file copied to: $dest_file"
