username=input("enter username:")
password=input("enter password:")
if username.lower()=="admin" and password =="1234":
    print("login successfull")

else:
    print("invalid login")
    print("attempts remaining:2")

    username=input("enter username:")
    password=input("enterpassword:")
    if username.lower()=="admin" and password=="1234":
        print("login successfull")
    else:
        print("ivalid login")
        print("attempts remaining:1")

        username=input("enter username:")
        password=input("enter password:")
        if username.lower()=="admin" and password=="1234":
            print("login successfull")
        else:
            print("inavalid login")
            print("attempts remaining:0")
            print("account locked")
            