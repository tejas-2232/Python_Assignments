
def login_page_backend():

    username = input("enter username:")
    password = input("enter password:")
    retype_password = input("retype password:")
    count = 0
    if password == retype_password:
        print("login successful")
    else:
        print("login failed, try again")
        while count < 3:
            password = input("Re-enter password:")
            retype_password = input("retype new password:")
            count += 1
            if password == retype_password:
                print("login successful")
                break
            else:
                print("Sorry, you entered wrong password more than allowed attempts, try again after some time")


if __name__ == "__main__":
    login_page_backend()
