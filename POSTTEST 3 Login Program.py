#   Program Login   #

user = ['Naf']
pw = ['12345']
choices = ""

print("""
|---------------------------------------------------|                                                   
|              Welcome to Our Website               |
|      ======================================       |                                          
|---------------------------------------------------|                                                   
""")

print("""
|---------------------------------------------------|                                                   
|               What do  You Want to do :           |
|               1. Login with Account               |
|               2. Create an Account                |
|               3. Exit Program                     |
|     ======================================        |                                          
|---------------------------------------------------|     
""")

def MainMenu():
    choices = input("Choose one number based of what you want to do = ")
    if choices == '1':
        TryAttempt = 0
        while TryAttempt <3 :
            username = input("Please input your username = ")
            password = input("Please input your Password = ")
            if username in user:
                x = user.index(username)
                if password == pw[x]:
                    print("\n======================")
                    print('Anda Berhasil Login')
                    print('Returning to menu...')
                    print("======================")
                    MainMenu()
                else:
                    print("\n======================")
                    print('Username/Password Wrong') 
                    print("======================")        
            else:
                print("\n======================")
                print('Username/Password Wrong')
                print("======================")
                
            TryAttempt +=1

            if TryAttempt >= 3:
                print("\n=======================================================")
                print ("You Cant do Another Login. Please wait another minutes")
                print ("Exiting program...")
                print("=======================================================")
                SystemExit
                break
    
    elif choices == '2':
        print("=" * 45)
        new_user = {}
        new_user['UserName'] = input("Create your username = ")
        new_user['Password'] = input("Create your password = ")

        user.append(new_user['UserName'])
        pw.append(new_user['Password'])

        print("=" * 45)
        print("Congrats, Your Account has been Created!")
        print("=" * 45)

        print("Returning to main menu...")
        print("=" * 45)
        MainMenu()
    else:
        print("=" * 30)
        print("Thanks For using our website")
        print("=" * 30)
        exit()
MainMenu()