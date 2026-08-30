# super keyword => is used to accsess the all thing from base class

class FBSStudent:

    st_cnt = 0

    def __init__(self, frn,name,batch):
        self.FRN = frn
        self.name = name
        self.batch = batch

        FBSStudent.st_cnt +=1

    def getFrn(self):
        return self.FRN

    def setFrn(self,frn):
        self.FRN = frn

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getBatch(self):
        return self.batch
    


    def display(self):
        print(f"FRN ={self.FRN}")
        print(f"Name = {self.name}")
        print(f"Batch = {self.batch}")



# FBS STUDENT END..................
class PlStud(FBSStudent):

    def __init__(self, frn, name, batch):
        super().__init__(frn, name, batch)

        self.cName = self.cName



    def display(self):
        super().display() 
        print(f"CName = {self.cName}")


s1 = FBSStudent(45,'Rohit Shrama','April30') 
s1.display()