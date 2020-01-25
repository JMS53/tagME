class Adress:
    def __init__(self, street='', num=0, zip=0, city='', country=''):
        self.street = street
        self.num = num
        self.zip = zip
        self.city = city
        self.country = country
    
    def __str__(self):
        a = self.street + " " + str(self.num)
        a += "\n"
        a += str(self.zip) + " " + self.city
        a += "\n" + self.country
        return a 
        
class Note:
    def __init__(self, author, content):
        self.author = author
        self.content = content
    
    def __str__(self):
        s = "Author: " + self.author
        s += "\n\n" + self.content
        return s

class POI:
    def __init__ (self, lat = False, lon = False, name=''):
        #validate user input
        
        if lat < -90 or lat > 90:
            print("lattitude out of bounds: ",  lat, " should be between -90 and 90")
            return None
        if lon < -180 or lon > 180:
            print("longitude out of bounds: ", lon, " should be between -180 and 180")
            return None
        
        #attributes
        self.lat = lat
        self.lon = lon
        self.adress = None
        self.noteL = 0 #number of 
        self.notes = {}
        self.tags = []
        self.name = name 
        
    def addAdress(self, str, num, zip, city, country):
        self.adress = Adress(str, num, zip, city, country)
    
    def removeAdress(self):
        self.adress = None
    
    def rename(self, name):
        self.name = name
    
    def addNote(self, auth, content):
        n = Note(auth, content)
        self.noteL += 1
        k = self.noteL
        self.notes[k] = n
    
    def rmNote(self, key, auth):
        if key in  self.notes.keys():
            self.notes[key] = Note(auth, 'Note deleted by: ' + auth)
    
    def showNotes(self):
        for i in range(self.noteL):
            j = i + 1
            print("Note ", j)
            print(self.notes[j])
            
            
    def showNote(self, key):
        if key in self.notes.keys():
            print("Note ", key)
            print("Author: ", self.notes[key].author)
            print("Content: ",self.notes[key].content, "\n")
    
    def __str__(self):
        s = "Name: "
        if self.name != '':
            s  += self.name + "\n"
        else:
            s += "Unamed POI\n"
            
        s += "Lattitude: " + str(self.lat) + "\n"
        s += "Longitude: " + str(self.lon) + "\n"
        if self.adress:
            s += str(self.adress)
        for k in range(self.noteL):
            s += "Note ID: " + str(k+1) + "\n"
            s += str(self.notes[k+1])
            s += "\n"
        return s
    
    



