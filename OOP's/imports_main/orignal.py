import demo1

def useIt():
    print("i am in use it..")
    print(__name__)
    demo1.add()


if __name__ == "__main__":
    useIt()