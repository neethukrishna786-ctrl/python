#1.given a list of numbers,write a program to find the sum of all numbers ,the sum of even numbers ,and the sum of odd numbers using list comprehension 
#numbers =[1,2,3,4,5,6,7,8,9,10]
#total = sum ([x for x in numbers])
#even_sum = sum ([x for x in numbers if x%2==0])
#odd_sum = sum ([x for x in numbers if x%2==1])
#print("sum of all numbers:",total)
#print("sum of even numbers:",even_sum)
#print("sum of odd numbers:",odd_sum)

#2. given a list of numbers ,create a new list that contains only numbers greter than 10 and divisible by 3 using list comprehension .
#numbers = [5,12,15,8,18,20,21,9]
#result=[num for num in numbers if num>10 and num%3==0]
#print(result)

#3.given a list of numbers,create a new list containing only even numbers greater than 10 using list comprehension.
#numbers=[5,12,15,18,20,7,24,9]
#result=[num for num in numbers if num>10 and num%2==0]
#print(result)

#4.given a list of strings ,create a new list containing the length of each string using list comprehension
#words=["apple","banana","grapes"]
#result=[len(word) for word in words]
#print(result)

#5.given a list of numbers ,create a new list where:
# even numbers are replaced with "even"
# odd numbers are replaced with "odd"
numbers=[1,2,3,4,5,6,7,8,9,10]
result=["even" if num%2==0 else "odd" for num in numbers]
print(result) 