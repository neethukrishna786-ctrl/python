#4.write a program to count the number of lines present in a file.
#file = open("sample.txt","r")
#count=0
#for line in file:
#    count +=1
#print("number of lines:",count)
#file.close()

#5.write a program to count the number of words in a file.
#file=open("sample.txt","r")
#data=file.read()
#words=data.split()
#count=len(words)
#print("number of words:",count)
#file.close()

#6.Write a python program to copy the contents from one file into another file.
#f1=open("file 1.txt","r")
#data=f1.read()

#f2=open("file 2.txt","w")
#f2.write(data)

#f1.close()
#f2.close()
#print("file copied successfully")

#7.write a program to read a file and print only the tines that contain the word "python".
#f=open("sample.txt","r")
#for line in f:
#    if"python" in line:
#        print(line)
#f.close()

#8.write a program that reads numbers from a file and calculate their sum
f=open("numbers.txt","r")
total=0
for line in f:
    total=total+int(line)
f.close()
print("sum=",total)
