#!/usr/bin/env python3

import requests

# Define available HTTP methods
http_methods = {
    "GET": "GET",
    "POST": "POST",
    "PUT": "PUT",
    "DELETE": "DELETE",
    "HEAD": "HEAD",
    "PATCH": "PATCH",
    "OPTIONS": "OPTIONS",
}

# Prompt user for destination URL
destination_url = input("Enter the destination URL: ")

# Prompt user for HTTP method
selected_method = ""
while not selected_method:
    print("Select an HTTP method:")
    for method, name in http_methods.items():
        print(f"{method}: {name}")
    selected_method = input("Enter your selection: ")
    if selected_method not in http_methods:
        print("Invalid selection. Please try again.")
        selected_method = ""

# Confirm request with user
print(f"You are about to send a {http_methods[selected_method]} request to {destination_url}.")
confirmation = input("Are you sure you want to proceed? (y/N): ")
if confirmation.lower() != "y":
    print("Request aborted.")
    exit(0)

# Send request
try:
    response = requests.request(
        method=selected_method,
        url=destination_url,
    )
except requests.exceptions.RequestException as e:
    print(f"Error sending request: {e}")
    exit(1)

# Translate response code
status_code = response.status_code
http_code_translations = {
    200: "OK",
    301: "Moved Permanently",
    302: "Found",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    500: "Internal Server Error",
    503: "Service Unavailable",
}
print(f"Response code: {status_code} ({http_code_translations.get(status_code, 'Unknown')})")

# Print response headers
print("Response headers:")
for header, value in response.headers.items():
    print(f"{header}: {value}")

# Stretch goals:
# - Implement API authentication with requests.auth
# - Add timeouts using the `timeout` parameter in the requests.request function
# - Implement error handling using try/except blocks
