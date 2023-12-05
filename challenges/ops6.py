import os

# Declare and initialize three variables to store bash commands
command1 = "whoami"  # user's username
command2 = "ip a"    # network interface information
command3 = "lshw -short"  # short format of hardware information

# Execute the first command and store the result in result1
result1 = os.popen(command1).read()

# Print the result of the first command with a descriptive comment
print("Result of 'whoami' command:")  # first command result header
print(result1)  # Print 'whoami' command output

# Execute the second command and store the result in result2
result2 = os.popen(command2).read()

# Print the result of the second command with a descriptive comment
print("\nResult of 'ip a' command:")  # second command result header
print(result2)  # Print 'ip a' command output

# Execute the third command and store the result in result3
result3 = os.popen(command3).read()

# Print the result of the third command with a descriptive comment
print("\nResult of 'lshw -short' command:")  # third command result header
print(result3)  # Print 'lshw -short' command output
