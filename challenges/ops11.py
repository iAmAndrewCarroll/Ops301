#!/usr/bin/env python3

import psutil
import subprocess
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Install Psutil if not already installed
try:
    import psutil
except ImportError:
    subprocess.call(['pip', 'install', 'psutil'])

def get_cpu_info():
    cpu_times = psutil.cpu_times()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cpu_info = {
        'Timestamp': timestamp,
        'User Mode Time': getattr(cpu_times, 'user', None),
        'Kernel Mode Time': getattr(cpu_times, 'system', None),
        'Idle Time': getattr(cpu_times, 'idle', None),
        'Priority User Mode Time': getattr(cpu_times, 'nice', None),
        'I/O Wait Time': getattr(cpu_times, 'iowait', None),
        'Hardware Interrupt Time': getattr(cpu_times, 'irq', None),
        'Software Interrupt Time': getattr(cpu_times, 'softirq', None),
        'Virtualized Time': getattr(cpu_times, 'steal', None),
        'Virtual CPU Time': getattr(cpu_times, 'guest', None)
    }

    return cpu_info

def display_category_info(category, info):
    print(f"{category} Information:")
    print("Timestamp:", info['Timestamp'])
    print(category, "Time:", info[category])

def save_to_text_file(info):
    with open('cpu_info.txt', 'w') as file:
        for key, value in info.items():
            file.write(f'{key}: {value}\n')
    print("CPU information saved to 'cpu_info.txt'")

def email_info(file_path, recipient_email):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        msg = MIMEText(content)
        msg['Subject'] = 'CPU Information Report'
        msg['From'] = 'your_email@gmail.com'  # Replace with your email address
        msg['To'] = recipient_email

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('this would be your email addy', 'password')  # Replace with your email and password
        server.sendmail('this would be your email addy', recipient_email, msg.as_string())
        server.quit()
        print(f"CPU information sent to {recipient_email}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    while True:
        print("\nOptions:")
        print("1. User Mode Time")
        print("2. Kernel Mode Time")
        print("3. Idle Time")
        print("4. Priority User Mode Time")
        print("5. I/O Wait Time")
        print("6. Hardware Interrupt Time")
        print("7. Software Interrupt Time")
        print("8. Virtualized Time")
        print("9. Virtual CPU Time")
        print("10. Save CPU Information to File")
        print("11. Email CPU Information")
        print("12. Quit")
        
        choice = input("Enter your choice (1-12): ")

        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            categories = [
                'User Mode Time',
                'Kernel Mode Time',
                'Idle Time',
                'Priority User Mode Time',
                'I/O Wait Time',
                'Hardware Interrupt Time',
                'Software Interrupt Time',
                'Virtualized Time',
                'Virtual CPU Time'
            ]
            category = categories[int(choice) - 1]
            cpu_info = get_cpu_info()
            display_category_info(category, cpu_info)
        elif choice == '10':
            cpu_info = get_cpu_info()
            save_to_text_file(cpu_info)
        elif choice == '11':
            file_path = 'cpu_info.txt'
            recipient_email = input("Enter recipient email address: ")
            email_info(file_path, recipient_email)
        elif choice == '12':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option (1-12).")

if __name__ == "__main__":
    main()
