from emp import Emp;
class Hr(Emp):
    def __init__(self, id, name, sal,comm):
        super().__init__(id, name, sal)
        self.comm=comm

    def getcomm(self):
        return self.comm
    def setcomm(self,comm):
        self.comm =comm

    def calSal(self):
        return self.comm +self.sal


    def __str__(self):
        return super().__str__()+f"commision={self.comm}"