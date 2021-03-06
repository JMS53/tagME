#! /usr/bin/env python3

import sys
import json

from POI import POI



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
1)  Add a new location 
2)  Add a physical adress to an existing location
3)  Rename an existing location 
4)  Add a note to an existing location
5)  Remove a note from an existing location
6)  Show all the information for an existing location
7)  Show a specific note for an existing location
8)  Show all locations
9)  Close the program & delete everything
10) Export data to JSON
11) Import from JSON
"""

pois = []

def addLoc():
    print( """
    New POIs are created using latitude (-90-90), longitude 
    (-180 - 180) and optional name.
    """)
    print("Please enter the latitude")
    lat = int(input())
    print("Please enter the longitude")
    lon = int(input())
    print("If you want to name the POI enter it now, else leave it blank")
    name = input()
    p = POI(lat, lon, name)
    pois.append(p)
        
def addAdr():
    print("Please enter the POI id")
    print("Leave blank to return to previous screen")
    id = int(input())
    if id == '':
        return 0
    if id >= 0 and id < len(pois):
        print("Please enter street name")
        street = input()
        print("Please enter adress number")
        num = int(input())
        print("Please enter the zip code")
        zip = input()
        print("Please enter the city")
        city = input()
        print("Please enter the country")
        country = input()
        p = pois[id]
        p.addAdress(street, num, zip, city, country)
        pois[id] = p
        return 1
    return 0
    
def addName():
    print("Please enter the POI id")
    print("Leave blank to return to previous screen")
    id = int(input())
    if id == '':
        return 0
    if id >= 0 and id < len(pois):
        print("Please enter a name for the POI")
        print("Leave blank to remove the name from a POI")
        name = input()
        p =pois[id]
        p.rename(name)
        pois[id] = p
        return 1
    return 0

def addNote():
    print("Please enter the POI id")
    print("Leave blank to return to previous screen")
    id = input()
    if id == '':
        return 0
    id = int(id)
    p = pois[id]
    print("Please enter your additional information for the POI")
    content = input()
    p.addNote(auth, content)
    pois[id] = p

def rmNotefromPOI():
    print("Please enter the POI id")
    print("Leave blank to return to previous screen")
    id = input()
    if id == '':
        return 0
    id = int(id)
    p = pois[id]
    print("Please enter the note id you want to remove")
    key = int(input())
    p.rmNote(key, auth)
    pois[id] = p

def showPOI():
    print("Please enter the POI id")
    print("Leave blank to return to previous screen")
    id = input()
    if id == '':
        return 0
    id = int(id)
    p = pois[id]
    print(p)

def showNoteFromPOI():
    print("Please enter the POI id")
    print("Leave blank to return to previous screen")
    id = input()
    if id == '':
        return 0
    id = int(id)
    p = pois[id]
    print("Please select the Note to see")
    k = int(input())
    p.showNote(k)

def showPOIs():
    for i in range(len(pois)):
        p = pois[i]
        print("POI ID: ", i)
        print("POI name: ", p.name)
    
def abandon():
    sys.exit()
 
def toJSON(fn = 'pois.json'):
    x = {"pois" : []}
    for p in pois:
        x["pois"].append(p.toJSON())
    
    y = json.dumps(x, indent=4)
    
    with open(fn, 'w') as outfile:
        outfile.write(y)
    

def fromJson(fn = 'pois.json'):
    with open (fn) as jsonFile:
        data = json.load(jsonFile)
        for p in data['pois']:
            
            point = POI(p['lat'], p['lon'], p['name'])
            
            if p['notes']:
               notes = p['notes'] 
               for k in notes.keys():
                  print(k)
                  n = notes[k]
                  auth = n['author']
                  cont = n['content']
                  point.addNote(auth,cont)
                
        pois.append(point)

    

print(welcomeText)

print("Please enter your id")
auth = input()




while True:
    print(actionText)
    choice = int(input())
    if choice == 1:
        addLoc()
    elif choice == 2:
        addAdr()
    elif choice == 3:
        addName()
    elif choice == 4:
        addNote()    
    elif choice == 5:
        rmNotefromPOI()
    elif choice == 6:
        showPOI()
    elif choice == 7:
        showNoteFromPOI()
    elif choice == 8:
        showPOIs()
    elif choice == 9:
        abandon()
    elif choice == 10:
        print("Please enter the filename to use, leave blank for pois.json")
        fn = input()
        if fn != '':
            toJSON(fn)
        else:
            toJSON()
    elif choice == 11:
        fromJson()
    else:
        print("Invalid input")

    
    
