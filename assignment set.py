#create a set with values(1,2,3,4)
my_set={1,2,3,4}
print(my_set)

#add the value 5 to the set{1,2,3,4} using a set method.
my_set={1,2,3,4}
my_set.add(5)
print(my_set)

#remove the value 3 from the set {1,2,3,4} using a set method.
my_set={1,2,3,4}
my_set.remove(3)
print(my_set)

#check if 2 exists in the set{1,2,3,4}
my_set={1,2,3,4}
print(2 in my_set)

#convert the list [1,2,2,3,4,4] into a set to remove duplicates.
list=[1,2,2,3,4,4]
result=set(list)
print(result)

#convert the tuple (10,20,30) into a set.
tuple=(10,20,30)
result=set(tuple)
print(result)

#find the union of sets{1,2,3} and{3,4,5}
set1={1,2,3}
set2={3,4,5}
result=set1.union(set2)
print(result)

#find the intersection of sets{1,2,3} and {3,4,5}
set1={1,2,3}
set2={3,4,5}
result=set1&set2
print(result)

#find the difference between sets {1,2,3,4} and {3,4}
set1={1,2,3,4}
set2={3,4}
result=set1-set2
print(result)

#create a copy of the set {5,6,7} using set method
my_set={5,6,7}
my_set.copy()
print(my_set)

#remove all elements from the set {1,2,3}using one set method.
my_set={1,2,3}
my_set.clear()
print(my_set)

#check whether {1,2} is a subset of {1,2,3}
set1={1,2}
set2={1,2,3}
print(set1.issubset(set2))

#check whether{1,2,3} is a superset of{1,2}
set1={1,2,3}
set2={1,2}
print(set1.issuperset(set2))

#find the symmetric difference between{1,2,3} and{3,4,5}
set1={1,2,3}
set2={3,4,5}
result=set1^set2
print(result)

#add multiple elements {8,9,10} into{1,2,3} using a set method.
set={1,2,3}
set.update([8,9,10])
print(set)

#remove a random element from a set {1,2,3} using a set method.
my_set={1,2,3}
removed_item=my_set.pop()
print(removed_item)

#check if two sets{1,2,3} and {3,2,1} are equal.
set1={1,2,3}
set2={3,2,1}
#print(set1==set2)

#from {1,2,3,4,5} ,remove {2,4} using a set method
set1={1,2,3,4,5}
set2={2,4}
set1.difference_update(set2)
print(set1)

