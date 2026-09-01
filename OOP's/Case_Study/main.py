from emp_manage import EmpManage
class Main:
    def login():
        print('Login Page')

        uid = 'admin'
        passw = '1234'

        username =input('enter username: ')
        password =input('enter passward: ')

        if(uid == username and passw == password):
            print('\nlogin sucessfully..\n')
            emp =EmpManage()

            while True:
                print("\n Print the Number to Perform Operations")
                print("\n1. Add Emp")
                print("2. Display Emp")
                print("3. Search Emp")
                print("4. Update Emp")
                print("5. Delete Emp")
                print("6. Exit")

                ch = int(input("Enter the choice: "))

                if ch == 1:
                    emp.addEmp()
                    print("Emp Added")

                elif ch == 2:
                    print("Display Employees Details \n")
                    emp.displayEmp()

                elif ch == 3:
                    print("Searching Employees Details...")
                    emp.searchEmp()

                elif ch == 4:
                    emp.updateEmp()

                elif ch == 5:
                    emp.delEmp()

                elif ch == 6:
                    emp.ExistEmp()
                    print("Thank you for Visit!")
                    break

                else:
                    print("Invalid choice!")

        else:
            print("Invalid UserName or Password..")


Main.login()