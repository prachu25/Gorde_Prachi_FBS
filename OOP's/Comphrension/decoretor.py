def demo(fun):
    print(("decorator is called.."))

    def wrapper():
        print("Before calling your function all task will be performed here..")
        fun()
        print("After Calling your function all task will be perforemd here..")

    return wrapper


@demo
def login():
    print("\n Login Demo \n")

@demo
def logout():
    print("\n Logout is Done \n")


login()

logout()
