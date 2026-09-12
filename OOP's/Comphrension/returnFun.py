# return inner Function from outer function

def outer():
    print("Outer Is called")

    def innerFunction():
        print("Inner FUnction is called")

    return innerFunction

a = outer()    # outer is called
a()            # it called = inner function is called

