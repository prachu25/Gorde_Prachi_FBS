class Project:

    # constructor
    def __init__(self, title, technology, duration):

        self.title = title
        self.tech = technology
        self.duration_time = duration

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getTechnology(self):
        return self.tech 
    
    def setTechnology(self, tech):
        self.tech = tech

    def getDurationTime(self):
            return self.duration_time
    
    def setDurationTime(self, duration):
        self.duration_time = duration



    def display(self): 
        print("\n----- Project Details -----")   
        print(f"Title   : {self.getTitle()}")
        print(f"Technology  : {self.getTechnology()}")
        print(f"Duration   : {self.getDurationTime()}")



proj = Project("Smart City", "Python", "2 Months")

print(proj.getTitle())

proj.setTechnology('Java')
proj.setDurationTime("4 months")

proj.display()
