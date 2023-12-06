#!/usr/bin/env python3

import os

# Function to generate directory structure and files
def generate_directory_structure(user_path):
    for (root, dirs, files) in os.walk(user_path):
        # Print the current directory
        print("Current Directory:", root)

        # Print subdirectories
        print("Subdirectories:", dirs)

        # Print files
        print("Files:", files)

# Main function
if __name__ == "__main__":
    # Ask the user for a directory path
    user_path = input("Enter a directory path: ")

    # Call the function to generate directory structure
    generate_directory_structure(user_path)
