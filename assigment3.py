#1.create a dictionary with keys "name" and "age" and values "nik" and 20
my_dict={"name":"nik","age":20}
print(my_dict)

#2.access the value of key "name" from {"name":"nik","age":20}
my_dict={"name":"nik","age":20}
print(my_dict["name"])

#3.add a new key "city" with value "delhi" to {"name":"nik","age":20}
my_dict={"name":"nik","age":20}
my_dict["city"]="delhi"
print(my_dict)

#4.update the value of "age" to 25 in {"name":"nik","age":20}
my_dict={"name":"nik","age":20}
my_dict.update({"age":25})
print(my_dict)

#5.delete the key "age" from {"name":"nik","age":20}
my_dict={"name":"nik","age":20}
del my_dict["age"]
print(my_dict)

#6.check if the key "email" exists in {"name":"nik","age":20}
data={"name":"nik","age":20}
print("email" in data.keys())

#7.get all keys from {"name":"nik","age":20} using a dictionary method.
my_dict={"name":"nik","age":20}
print(my_dict.keys())

#8.get all values from {"name":"nik","age":20} using a dictionary method.
my_dict={"name":"nik","age":20}
print(my_dict.values())

#9.convert the dictionary ("a":1,"b":2) into list of (key,value) pairs.
data={"a":1,"b":2}
result=list(data.items())
print(result)

#10.create a dictionary from two lists:(use zip method) keys=["name","age"] values=["nik",20].
keys=["name","age"]
values=["nik",20]
data=dict(zip(keys,values))
print(data)

#11.count how many keys are in {"a":1,"b":2,"c":3}
data={"a":1,"b":2,"c":3}
print(len(data))

#12.merge two dictionaries {"a":1} and {"b":2} into one.
dict1={"a":1}
dict2={"b":2}
dict1.update(dict2)
print(dict1)

#13.clear all elements from {"a":1,"b":2} using a dictionary method.
my_dict={"a":1,"b":2}
my_dict.clear()
print(my_dict)

#14.copy the dictionary {"x":10,"y":20} using a dictionary method.
my_dict={"x":10,"y":20}
my_dict.copy()
print(my_dict)

#15.get the value of key "salary" safely from {"name":"nik","age":20} without getting an error.
my_dict={"name":"nik","age":20}
print(data.get("salary"))

#16.from {"a":1,"b":2,"c":3},remove the last inserted item using a dictionary method.
my_dict={"a":1,"b":2,"c":3}
last_item=my_dict.popitem()
print(last_item)

#17.given student ={"name":"rahul","marks":{"math":90,"science":85}}, access only the "science" marks.
student={"name":"rahul","marks":{"math":90,"science":85}}
print(student["marks"]["science"])

#18.from the above student dictionary,update "math" marks to 95.
student={"name":"rahul","marks":{"math":90,"science":85}} 
student["marks"]["math"]=95
print(student)

#19.add a new subject "english":88 inside the "marks"dictionary.
student={"name":"rahul","marks":{"math":90,"science":85}}
student["marks"]["english"]=88
print(student)

#20.delete the subject "science" fom inside "marks".
student={"name":"rahul","marks":{"math":90,"science":85}}
del student["marks"]["science"]
print(student)






