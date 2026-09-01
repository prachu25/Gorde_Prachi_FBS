from emp import Emp
class Dev(Emp):
    def __init__(self, id, name, sal,bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus

    def getbonus(self):
        return self.bonus
    def setbonus(self,bonus):
        self.bonus=bonus

    def calSal(self):
        return self.bonus + self.sal  #it gives output
    
    # def calSal(self):
    #     return super().calSal()+self.bonus // none+5000 we cannot add
    

    def __str__(self):
        return super().__str__()+f"Bonus={self.bonus}"