# reading the people's json file
# and creates a variable (person) with all the data contained
import json
import termcolor
from pathlib import Path

# -- Read the json file
json_string = Path("people-1.json").read_text()

# Create the object person from the json string
person = json.loads(json_string)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# -- Read the Firstname
firstname = person['Firstname']
lastname = person['Lastname']
age = person['age']

# Print the information on the console, in colors
print()
termcolor.cprint("Name: ", 'green', end="")
print(firstname, lastname)
termcolor.cprint("Age: ", 'green', end="")
print(age)
