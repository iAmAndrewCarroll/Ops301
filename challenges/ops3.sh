#!/bin/bash

# prompt for dir path
read -p "Enter a directory path: " dir

# check if dir exists
if [ -d "$dir" ]; then
  # nav to dir
  cd "$dir"

  # see current permissions
  read -p "Do you want to see current permissions? (y/n): " show

  if [ "$show" == "y" ]; then
    # print permissions
    echo "Current Permissions:"
    ls -l
  fi

  # prompt for new permissions
  read -p "Do you want to change permissions? (y/n): " change

  if [ "$change" == "y" ]; then
    # prompt for new permissions
    read -p "Enter new permissions (ex: 777, 400, etc): " perms

    # change permissions
    chmod -R "$perms" .

    # print new permissions
    echo "New Permissions: $perms"
  fi
else
  echo "The directory $dir does not exist."
fi