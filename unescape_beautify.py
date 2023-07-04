import json
import pyperclip

def process_json(input_string):
    # Remove slashes
    no_slashes = input_string.replace("\\", "")

    # Replace single quotes with double quotes
    double_quotes = no_slashes.replace("'", "\"")

    return double_quotes

# Receive JSON as input string
json_string = input("Enter the JSON string: ")

# Process the JSON
modified_json = process_json(json_string)

# Print the modified JSON
print("Modified JSON:")
print(modified_json)

# Beautify the JSON
try:
    beautified_json = json.dumps(json.loads(modified_json), indent=4)
    print("Beautified JSON:")
    print(beautified_json)

    # Copy to clipboard
    pyperclip.copy(beautified_json)
    print("Beautified JSON copied to clipboard.")
except json.JSONDecodeError:
    print("Invalid JSON string. Please check your input.")

# Ask for new input
new_json = input("Enter a new JSON string: ")
print("New JSON:")
print(new_json)
