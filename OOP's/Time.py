class Time:

    def __init__(self, hr, minu, sec):
        self.hr = hr
        self.minu = minu
        self.sec = sec

    def getHr(self):
        return self.hr

    def setHr(self, hr):
        self.hr = hr

    def getMin(self):
        return self.min

    def setMin(self, minu):
        self.minu = minu

    def getSec(self):
        return self.sec

    def setSec(self, sec):
        self.sec = sec

    def __add__(self, other):
        totalsec = self.sec+other.sec
        totalminu = self.minu+other.minu
        totalhr = self.hr+other.hr
        return Time(totalhr,totalminu,totalsec)

    def __str__(self):
        return (f"Hour: {self.hr} \t Minute: {self.minu} \t Second: {self.sec}")



t1 = Time(12, 36, 49)
t2 = Time(11, 12, 1)


print(t1 + t2)         # TypeError: unsupported operand type(s) for +: 'Time' and 'Time'
# print(type(t1))


                     















