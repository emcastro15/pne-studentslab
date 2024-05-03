import json
import termcolor
from pathlib import Path

# -- Read the json file
json_string = Path("people-e1.json").read_text()

# Create the object person from the json string
people = json.loads(json_string)

print(f"Total people in the database: {len(people)}")

# Print the information on the console, in colors
for person in people:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])

    # Get the phoneNumber list
    phoneNumbers = person['phoneNumber']

    # Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, dict_of_numb in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("\t- Type: ", 'red', end='')
        print(dict_of_numb['type'])
        termcolor.cprint("\t- Number: ", 'red', end='')
        print(dict_of_numb['number'])