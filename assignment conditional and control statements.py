#1. write a program to check whether a number is positive ,negative,or zero
#num=int(input("enter a number:"))
#if num >0:
#    print("The number is positive")
#elif num <0:
#    print("The number is negative")
#else:
#    print("The number is zero")

#2.check if a number is even or odd
#num=int(input("enter a number:"))
#if num % 2 ==0:
#    print("even number")
#else:
#    print("odd number")

#3.Given a number,check if it is greater than 100
#x=110
#if x>100:
#    print("x is greater than 100")

#4.Check whether a person is eligible to vote (age>=18)
#age=int(input("enter your age:"))
#if age>=18:
#    print("eligibele to vote")
#else:
#    print("not eligible to vote")

#5.Given two numbers,print the greater number.
#a=10
#b=20
#if a>b:
#    print("greater number is :",a)
#elif b>a:
#    print("greater number is:",b)
#else:
#    print("both are equal")

#6.Given three numbers, print the largest number
#x=10
#y=20
#z=30
#if x>=y and x>=z:
#    print("largest number is:",x)
#elif y>=x and y>=z:
#    print("largest number is:",y)
#else:
#    print("largest number is z")

#7.Check whether a year is leap year
#year=int(input("enter a year:"))
#if year % 400==0:
#    print("leap year")
#elif year %100==0:
#    print("leap year")
#elif year %4==0:
#    print("leap year")
#else:
#    print("not a leap year")

#8.Given a mark ,print: "pass" if marks>=40,"fail" otherwise.
#marks= int(input("enter a number:"))
#if marks>=40:
#    print("pass")
#else:
#    print("fail")

#9.Given a mark, print grades:a>=90,b>=75,c>=60,fail:below 60
#marks=int(input("enter your mark:"))
#if marks>=90:
#    print("grade A")
#elif marks>=75:
#    print("grade B")
#elif marks>=60:
#    print("grade C")
#else:
#    print("fail")        

#10.Check if a character is a vowel or consonant
#ch = input("enter a character:")
#if ch in "aeiouAEIOU":
#    print("vowel")
#else: print("consonant")

#11.print numbers from 1 to 10 but stop when number is 6
#for i in range(1,11):
#    if i==6:
#        break
#    print(i)

#12.print numbers from 1 to 10 but skip number 5.
#for i in range(1,11):
#    if i==5:
#        continue
#    print(i)

#13.use pass inside an if block and explain why it doesn't cause an error.
#num=10
#if num>0:
#    pass
#print("program executed successfully")

#14.print all even numbers between 1 and 20
#for i in range(1,21):
#    if i % 2==0:
#        print(i)

#15.Find the sum of numbers from 1 to 10
#sum =0
#for i in range(1,11):
#    sum=sum+i
#print("sum=",sum)

#16.Check whether a given number is multiple of both 3 and 5
#num =int(input("enter a number:"))
#if num %3==0 and num%5==0:
#    print("number is mutiple of both 3 and 5")
#else:
#    print("not a multiple of 3 and 5")

#17.print "hello" 5 times using a loop.
#for i in range(5):
#    print("hello")

#18.Given a list [1,2,3,4,5],print only numbers greater than 3.
#numbers=[1,2,3,4,5]
#for i in numbers:
#    if i >3:
#        print(i)

#19.write a python program to stimulate a login system with the following rules:
#the correct user name is "admin" and the correct password is "1234".
#the user is allowed a maximum of 3 login attempts.
#the username comparison should be case-insensitive.
#the password comparison should be case-sensitive.
#if the user enters correct credentials within the allowed attempts,display login successful.
#if all attempts are used without success,display account locked.
#after each failed atempt,display the number of attempts remaining.

#20.write a python program that acts as a traffic light controller with the following conditions:
#the program should accept either a color or number as input.
#use the mapping:
#1 or "red" stop and wait for 60 seconds
#2 or "yellow" ready and wait for 5 seconds
#3.or "green" go and drive safely
#the program should handle inputs in a case insensitive manner.
#if the input does not match any valid color or number,display invalid signal.
signal=input("enter traffic signal(red/yellow/green or 1/2/3):")
signal =signal.lower()
if signal =="1" or signal =="red":
    print("stop and wait for 60 seconds")
elif signal == "2" or signal =="yellow":
    print("ready and wait for 5 seconds")
elif signal =="3" or signal =="green":
    print("go and drive safely")
else:
    print("invalid signal")

