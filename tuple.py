a=(1,2,3,'python',4.5)
print(a)

s=(8,)
print(type(s))

b=('apple','banana','cherry')
print(b[2])
print(b[-2])

a=(20,40,60,80)
print(a[1:3])

s=(1,2,3)
s=(4,5,6)
print(s)

s=('apple','banana','cherry')
a=list(s)
a[1]='orange'
s=tuple(a)
print(s)

a=('apple','banana','cherry')
(f1,f2,f3)=a
print(f1)
print(f2)
print(f3)

s=(1,2,3,4,5)
(f,*m,l)=s
print(f)
print(m)
print(l)

tuple1=(3,4,5)
tuple2=(6,7,8)
s=tuple1+tuple2
print(s)

s=(1,2,4,4,5,4)
print(s.count(4))

s=('apple','banana','cherry')
print(s.index('cherry'))

s=('apple','banana','cherry')
del s
print(s)
