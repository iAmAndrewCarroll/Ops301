#!/usr/bin/env python3
# Script:                       Ops Challenge 10 - Super Troopers
# Author:                       Andrew Carroll
# Date of latest revision:      12/8/23
# Purpose:                      File Handling in Python

import os

# Variable Declarations

# Create a new movie file named "SuperTroopers.txt"
movie_path = "SuperTroopers.txt"

# Main

# Open the movie file with write permissions and assign it to the "movie" variable
with open(movie_path, "w") as movie:
  # Write three lines (data) related to "Super Troopers" to the movie file
  movie.write("Super Troopers\n")
  movie.write("A comedy about five Vermont state troopers who get into various shenanigans.\n")
  movie.write("Do I look like a cat to you, boy? Am I jumpin' around all nimbly bimbly from tree to tree?\n")

# Read the contents of the movie file
with open(movie_path, "r") as movie:
  # Read the first line of the file and print it
  first_line = movie.readline()
  print("First line:", first_line.strip())

# Close the movie file
movie.close()

# Remove the movie file
os.remove(movie_path)

# End
