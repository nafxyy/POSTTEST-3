#   Login Simple   #

print("==============================")
print("    Welcome to Our Website!   ")
print("==============================")

user = {'Naf' : '12345'}

x = 1

print("================================================")
print("What do you want to do? \n1. Login With Your Account. \n2. Create Another Account. \n3. Exit The Program")
print("================================================")

while x > 0:
    x +=1
    print("\n========================================================")
    chose = input("Choose one number based of what you want to do = ")

    if chose == "1":
        y = 1
        while y > 0:
            username = input("Please input your username = ")
            password = input("Please input your Password = ")
            if username in user and user[username] == password:
                print("===========================")
                print('Login has been successful!')
                print("===========================")

                print("\n============================")
                print("Returning to Main Menu...")
                print("============================")
                break

            else:
                print("=========================")
                print('Wrong Username or Password. \nTry Again')
                print("=========================")

                if y >= 3:
                    print("\n==================================================")
                    print("Cant do another attempt. Please try again later.")

                    print ("Exiting program...")
                    print("==================================================")
                    break
            y +=1

    elif chose == "2":
        print("============================================")
        NewUser = input("Create your username = ")
        NewPass = input("Create your password = ")
        user[NewUser] = NewPass
        print("============================================")

        print("\n============================================")
        print("Congrats, Your Account has been Created!")
        print("==============================================")

    elif chose == "3":
        print("==============================")
        print("Thanks For using our website")
        print("==============================")
        break

    else:
        print("Please type 1, 2 or 3")
