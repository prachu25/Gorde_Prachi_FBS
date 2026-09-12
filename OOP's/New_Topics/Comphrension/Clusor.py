
# Closure is a function that remembers variables from 
# its outer function even after the outer function has finished.
def outer():
    print("Outer Is called")
    var = "Ishan"

    def innerFunction():
        print("Inner FUnction is called..", var)

    return innerFunction

a = outer()    # outer is called
a()            # it called = inner function is called