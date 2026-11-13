my_list=[1,2,3,'python',4.5]
print(my_list)

my_list=['apple','banana','cherry']
print(my_list[1])
print(my_list[-1])

my_list=[10,20,30,40,50]
print(my_list[1:4])

my_list=['apple','banana','cherry']
my_list[1:3]=['a','b']
print(my_list)

my_list=['apple','banana']
my_list.append('cherry')
print(my_list)

my_list=['apple','banana']
my_list.insert(2,'cherry')
print(my_list)

my_list=['apple','banana']
new_list=['orange','grapes']
my_list.extend(new_list)
print(my_list)

my_list=['apple','banana','orange']
my_list.remove('banana')
print(my_list)

my_list=['apple','banana','orange']
popped_item=my_list.pop(1)
print(popped_item)
print(my_list)

my_list=['1','2','3','4','5']
del my_list[0]
print(my_list)

my_list=['a','b','c','d']
my_list.clear()
print(my_list)

my_list=[1,2,2,3,2,2,4,5,2]
print(my_list.count(2))

my_list=['apple','banana','cherry']
print(my_list.index('banana'))

my_list=[1,2,3]
my_list.reverse()
print(my_list)

my_list=[3,1,2]
my_list.sort()
print(my_list)

my_list=[1,2,3]
copied_list=my_list.copy()
print(copied_list)

numbers=[3,5,1,4,2]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

my_list=[3,1,4]
sorted_list=sorted(my_list)
print(sorted_list)

original_list=['apple','orange','cherry']
copied_list=original_list.copy()
copied_list=original_list[:]
print(copied_list)

list1=['apple','banana']
list2=['cherry','orange']
list=list1+list2
print(list)

list1=['apple','banana']
list2=['cherry','orange']
list1.extend(list2)
print(list1)