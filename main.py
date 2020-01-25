#! /usr/bin/env python3

import POI



welcomeText = """The aim of this tool is to provide a means of logging locations and 
adding information to these by various users. You will be asked to 
provide an id, this is in order to provide authorship to the notes you 
add for a given location.

For location, please us Longitude and latitude (-90-90, -180-180) as
these values are validated.

Data is currently only stored as long as main.py is running - killing 
this task will effectively delete all your work.
"""

actionText = """
Please select from the following options:
1) Add a new location 
2) Add a physical adress to an existing location
3) Rename an existing location a name
4) Add a note to an existing location
5) Remove a note from an existing location
6) Show all the information for an existing location
7) Show a specific note for an existing location
8) Show all locations

"""

print(welcomeText)

print("Please enter your id")
auth = input()

pois = []
