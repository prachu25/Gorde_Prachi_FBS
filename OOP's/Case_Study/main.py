class Login:

    def login(self):

        userrid = "admin"
        password = "1234"

        uname = input("Enter UserName: ")
        passw = input("Enter Password: ")

        if uname == userrid and passw == password:
            print("\nLogin Successful...")

            while True:
                print("\nEnter 1 for Add Emp")
                print("Enter 2 for Display Emp")
                print("Enter 3 for Search Emp")
                print("Enter 4 for Update Emp")
                print("Enter 5 for Delete Emp")
                print("Enter 6 for Exit")

                ch = int(input("Enter the choice: "))

                if ch == 1:
                    print("Add")

                elif ch == 2:
                    print("Display")

                elif ch == 3:
                    print("Search")

                elif ch == 4:
                    print("Update")

                elif ch == 5:
                    print("Delete")

                elif ch == 6:
                    print("Thank you for Visit!")
                    break

                else:
                    print("Invalid choice!")

        else:
            print("Invalid UserName or Password..")


obj = Login()
obj.login()