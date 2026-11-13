t=(1,2,3)
print(t[2])

t=(10,20,30)
s=list(t)
print(s)

l=[1,2,3]
t=tuple(l)
print(t)

t=("a","b","c","d")
print(t[1:3])

t=("x","y","z")
print("x" in t)

t=(5,3,9,1)
print(max(t))

t=(1,2,3)
new_t=t*2
print(new_t)

t=(1,2,2,3,2)
print(t.count(2))

t=("dog","cat","mouse")
print(t.index("cat"))

t=(1,2,3,4,5)
print(t[::-1])

t1=(1,2)
t2=(3,4)
r=t
t=t1+t2
print(t)

t="hello"
r=tuple(t)
print(r)

t=(1,2,3,4)
r=[t[0],t[-1]]
print(r)

t=(10,20,30,40)
s=list(t)
s[2]=99
r=tuple(s)
print(r)

t=(1,2,3)
a,b,c=t
print(a)
print(b)
print(c)

t=(1,2,3)
r=(t,)
print(r)

t=("a","b")
list=["c","d"]
r=t+tuple(list)
print(r)

t=(1,2,3)
print(t==t[::-1])

t=([1,2],[3,4])
result=[]
result.extend(t[0])
result.extend(t[1])
print(result)

t=(1,[2,3],4)
t[1].append(5)
print(t)
