from hr import Hr
from dev import Dev

class EmpManage:

    def __init__(self):
        self.addEmpDetails={}   # dict to store emp data temporary


    # ADD EMOLOYEE FUNCTION
    def addEmp(self):

        empid=int(input("Enter id of Emp:"))

        if empid in self.addEmpDetails:
            print("Emp Already Exist")
            return
        
        else:
            name =input("Enter name of Emp: ")
            sal = int(input("Enter salary of Emp: "))

            print("1 Hr")
            print("2 Dev")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                comm =float(input("Enter the commission of Hr:"))
                emp =Hr(empid,name,sal,comm)

            elif ch == 2:
                bonus =float(input("Enter the bonus of Deveploper:"))
                emp = Dev(empid,name,sal,bonus)

            else:
                print("Invalid choice......")
                return
            
            self.addEmpDetails[empid] =emp
            print("Emp added sucessfully...")


    # DISPLAY EMPLOYEE FUNCTION
    def displayEmp(self):
    
        print(self.addEmpDetails.values())

        for emp in self.addEmpDetails.values():
            print(emp)

        
    # SEARCH EMPLOYEE FUNCTION
    def searchEmp(self):
        if len(self.addEmpDetails) == 0:
            print("Employee not Exist...")
        else:
            eid = int(input("Enter id of Employee: "))

            if eid in self.addEmpDetails:
                print("Employee Found...")
                print(self.addEmpDetails[eid])
            else:
                print("Employee not Found...")



    # UPDATE EMP FUNCTION : NAME AND SALARY UPDATE
    def updateEmp(self):

        if len(self.addEmpDetails) == 0:
            print("Employee not Exist...")
        else:
            eid = int(input("Enter id of Employee: "))

            if eid in self.addEmpDetails:
                emp = self.addEmpDetails[eid]

                print("1. Update Name")
                print("2. Update Salary")

                ch = int(input("Enter your choice: "))

                if ch == 1:
                    name = input("Enter new name: ")
                    emp.setName(name)
                    print("Name Updated Successfully...")

                elif ch == 2:
                    sal = int(input("Enter new salary: "))
                    emp.setSal(sal)
                    print("Salary Updated Successfully...")

                else:
                    print("Invalid choice...")
            else:
                print("Employee not Found...")


    # DELETE EMP FUNCTION
    def delEmp(self):

        if len(self.addEmpDetails) == 0:
            print("Employee not Exist...")
        else:
            eid = int(input("Enter id of Employee: "))

            if eid in self.addEmpDetails:
                del self.addEmpDetails[eid]
                print("Employee Deleted Successfully...")
            else:
                print("Employee not Found...")


    # EXIT FUNCTION
    def ExistEmp(self):
        print("Logout sucessfully")