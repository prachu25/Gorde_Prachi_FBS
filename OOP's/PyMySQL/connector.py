import pymysql

try:
    connection = pymysql.connect(                               # put  your orginal value
    host="HOST_NAME",
    port="PORT",
    user="USER_NAME",
    password="PASSWORD_NAME",
    database="DATABASE_NAME"
    )

    print("DataBase connect Succesfully!!!\n")

    # create cursor
    cursor = connection.cursor()

    cursor.execute("select * from users")
    data = cursor.fetchall()

    # print(data)

    for i in data:
        print(i)


except pymysql.Error as e:
    print("Connection Failed!!")
    print(e)
