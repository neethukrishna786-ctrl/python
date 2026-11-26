#1.write a function that takes a number as input and returns whether the number is even or odd
#def even_odd(num):
#    if num%2==0:
#        return "even"
#    else:
#        return "odd"

#n=int(input("enter a number:"))
#print(even_odd(n))

#2.write a function that takes three numbers are input and returns the largest number among them
#def largest(a,b,c):
#    if a>b and a>c:
#        return a
#    elif b>a and b>c:
#        return b
#    else:
#        return c
#x=int(input("enter first number:"))
#y=int(input("enter second number:"))
#z=int(input("enter third number:"))
#print("largest number is:",largest(x,y,z))

#3.write a function that takes a list of numbers as input and returns the sum of all elements in the list.
#def sum_list(numbers):
#    total=0
#    for num in numbers:
#        total=total+num
#    return total

#numbers =[10,20,30,40,50]
#print("sum=",sum_list(numbers))

#4.write a function that takes a list of numbers as input and returns a new list containing only even numbers.

#def even_numbers(numbers):
#    result=[]
#    for num in numbers:
#        if num%2==0:
#            result.append(num)
#        return result
#numbers=[1,2,3,4,5,6,7,8]
#print("Even numbers:",even_numbers(numbers))

#5.write a function that takes a string as input and returns the lengthof the string.
#def string_length(s):
#    return len(s)
#text=input("enter a string:")
#print("length of string:",string_length(text))

#6.write a function that takes a string as input and returns the string in uppercase.
#def uppercase(s):
#    return s.upper()
#text=input("enter a string:")
#print("uppercase:",uppercase(text))

#7.write a function that takes a number as input and returns whether a number is positive ,negative,or zero.
#def check_number(num):
#    if num>0:
#        return "positive"
#    elif num<0:
#        return "negative"
#    else:
#        return "zero"
#n=int(input("enter a number:"))
#print(check_number(n))

#8.write a function that takes a number as input and returns true if the number is a multiple of both 3 and 5 ,otherwise returns false.
#def check(n):
#    if n % 3==0 and n % 5==0:
#        return True
#    else:
#        return False
#print(check(15))

#9.write a function that takes a list of numbers as input and returns the maximum value in the list.
#def maximum(numbers):
#    return max(numbers)
#print(maximum([10,20,5,40,30]))

#10.write a function that takes marks as input and returns the grade according to the following rules
#A for marks >=90
#B for marks >=75
#C for marks >=60
#Fail for marks below 60
#def grade(marks):
#    if marks >=90:
#        return "A"
#    elif marks>=75:
#        return "B"
#    elif marks >=60:
#        return "C"
#    else:
#        return "Fail" 
#print(grade(85))

#11.write a function that takes a price as input and returns the discounted price after applying a 10% discount
#def discount(price):
#    discounted_price =price -(price * 10/100)
#    return discounted_price
#print(discount(1000))

#12.write a function that takes a list of numbers as input and returns the count of even and odd numbers.
#def count_even_odd(numbers):
#    even =0
#    odd=0

#    for n in numbers:
#        if n % 2 ==0:
#            even +=1
#        else:
#            odd +=1
#    return even, odd
#print(count_even_odd([1,2,3,4,5,6]))

#13.write a function that takes a temperature in celsius as input and returns the temperature in fahrenheit.
#def celsius_to_fahrenheit(celsius):
#    fahrenheit = (celsius * 9/5)+32
#    return fahrenheit
#print(celsius_to_fahrenheit(25))
