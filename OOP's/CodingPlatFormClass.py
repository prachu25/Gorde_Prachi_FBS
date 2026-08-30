class CodingPlatForm:

    # COnstructor
    def __init__(self, platform, problem_solved, language):

        self.platform = platform
        self.problem_solved = problem_solved
        self.language = language


    def getPlatform(self):
        return self.platform

    def setPlatform(self,platform):
        self.platform = platform

    def getProblemSolved(self):
        return self.problem_solved
    
    def setProblemSolved(self,solved):
        self.problem_solved = solved

    def getLanguage(self):
        return self.language

    def setLanguage(self, lan):
        self.language = lan
    

    
        


    def display(self):
        print("\n--- Coding Details -----")
        print(f"Platform         : {self.getPlatform()}")
        print(f"Problems Solved  : {self.getProblemSolved()}")
        print(f"Language         : {self.getLanguage()}")
    

c = CodingPlatForm("Leetcode", 45, 'Java')
c.display()

c1 = CodingPlatForm("Coding Ninja", 45, 'Java')
c1.setLanguage('JavaScript')
c1.display()

# why we use constructor ?
# to init the state of an object 