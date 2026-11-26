#9.write a program to handle a value error when the user enters invalid input(for example,entering letters instead of a number).
#try:
#    num=int(input("enter a number:"))
#    print("number:",num)
#except ValueError:
#    print("invalid input! please enter a number.")

#10.write a program to handle invalid input(user enters a string instead of a number.)
#try:
#    a=int(input("enter first number:"))
#    b=int(input("enter second number:"))
#    print("sum:",a+b)
#except ValueError:
#    print("please enter numbers only.")

#11.write a program that handles file not found error while opening a file.
#try:
#    f=open("sample.txt.py","r")
#    print(f.read())
#    f.close()
#except FileNotFoundError:
#    print("file not found!")

#12.write a program using try,except,and else blocks.
#try:
#    a=int(input("enter first number:"))
#    b=int(input("enter second number:"))
#    result=a+b
#except ValueError:
#    print("invalid input!") 
#else:
#    print("sum:",result)

#13.write a program using try,except,and finally to ensure a message "program ended" is always printed.
#try:
#    num=int(input("entera number:"))
#    print("number:",num)
#except ValueError:
#    print("inavalid input!")
#finally:
#    print("program ended")

#14.write a program that catches multiple exceptions using multiple except blocks.
#try:
#    a=int(input("enter first number:"))
#    b=int(input("enter second number:"))
#    print("result:",a/b)
#except ValueError:
#    print("please enter number only.")
#except ZeroDivisionError:
#    print("cannot divide by zero.")

#15.write a program that raises a custom error when the user enters a negative number.
#num=int(input("enter a number:"))
#if num<0:
#    raise ValueError("negative numbers are not allowed")
#else:
#    print("number is:",num)

