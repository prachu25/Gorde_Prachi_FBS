import pickle
from emp import Emp

file = "employee.dat"

while True:

    print("\n1. Add")
    print("2. Search")
    print("3. Delete")
    print("4. Edit")
    print("5. Display")
    print("6. Exit")

    ch = int(input("Enter choice: "))


    ## ADD
    if ch == 1:
        eid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        basic = float(input("Enter Basic: "))

        emp = Emp(eid, name, basic)

        with open(file, "ab") as f:
            pickle.dump(emp,f)

        print("Record Added")


    ### Search
    elif ch == 2:
        eid = int(input("Enter ID: "))
        found = False

        try:
            with open(file, "rb") as f:
                while True:
                    try:
                        emp = pickle.load(f)

                        if emp.eid == eid:
                            emp.display()
                            found = True
                            break

                    except EOFError:
                        break

        except FileNotFoundError:
            pass

        if not found:
            print("Record not found!")


    ## DELETE
    elif ch == 3:
        eid = int(input("Enter ID: "))
        records = []

        try:
            with open(file,"rb") as f:
                while True:
                    try:
                        emp = pickle.load(f)
                        if emp.eid != eid:
                            records.append(emp)
                    except EOFError:
                        break

            with open(file,"wb") as f:
                for emp in records:
                    pickle.dump(emp,f)

            print("Record deleted!")

        except FileNotFoundError:
            print("No Records")


    ## EDIT 
    elif ch == 4:
        eid = int(input("Enter Id: "))
        records = []

        try:
            with open(file, "rb") as f:
                while True:
                    try:
                        emp = pickle.load(f)

                        if emp.eid == eid:
                            emp.ename = input("Enter new name: ")
                            emp.basic = float(input("Enter new basic: "))

                        records.append(emp)

                    except EOFError:
                        break


            with open(file, "wb") as f:
                for emp in records:
                    pickle.dump(emp, f)


            print("Records update")


        except FileNotFoundError:
            print("No Records")



    ## DISPLAY

    elif ch == 5:
        try:
            with open(file,"rb") as f:
                while True:
                    try:
                        emp = pickle.load(f)
                        emp.display()
                    except EOFError:
                        break

        except FileNotFoundError:
            print("No Records")


    ## EXIT
    elif ch == 6:
        break

    else:
        print("Invalid choice")



