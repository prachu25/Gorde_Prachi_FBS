from threading import Thread, Lock

lock = Lock()

def deposite(amt):
    lock.acquire()
    with open("balance.txt", 'r') as f:
        bal = int(f.read())
    bal = bal + amt

    with open("balance.txt", 'w') as f:
        f.write(str(bal))
    lock.release()

def withdraw(amt):
    lock.acquire()
    with open("balance.txt", 'r') as f:
        bal = int(f.read())
    bal = bal - amt

    with open("balance.txt", 'w') as f:
        f.write(str(bal))
    lock.release()



# Create threads
t1 = Thread(target=deposite, args=(20000,))
t2 = Thread(target=withdraw, args=(10000,))


t1.start()
t2.start()


print("Final Balance: ")
with open("balance.txt", "r") as f:
    print(f.read())