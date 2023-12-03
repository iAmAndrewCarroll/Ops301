#!/bin/bash

# menu function
menu() {
  echo "Main Menu:"
  echo "1. Hello World, may I have another?"
  echo "2. Ping Self"
  echo "3. IP Info"
  echo "4. Exit"
  echo "Make your selection, nerd: "
}

# display network adapter info
ip_info() {
  echo "Network Info: "
  ifconfig
}

# Loop
while true; do
  clear # clear screen for menu
  menu # display menu
  read choice # read user input

  case $choice in
    1) echo "Hello World, may I have another?";;
    2) echo "Pinging Self..."
       ping -c 4 127.0.0.1 # ping self
       ;;
    3) ip_info # display network info
       ;;
    4) echo "Exiting..."
       exit 0 # exit script
       ;;
    *) echo "Invalid Selection, try again nerd.";;
  esac

  # pause before clearing screen
  read -p "Press [Enter] to continue..."
done