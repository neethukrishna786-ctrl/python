s="hello"
print(s.upper())

s="python"
print(s.lower())

s="hello world"
new_s=s.replace("world","python")
print(new_s)

s="hello"
print(s[1:4])

s="python"
print(s[::-1])

s1="hello"
s2="world"
s=s1+","+s2
print(s)

words=["hi""hi""hi"]
sentence=" ".join(words)
print(sentence)

s="concatenate"
print("cat" in s)

s="banana"
print(s.count("a"))

s=" hello "
print(s.strip())

s="hello"
print(s.index("o"))

s="a,b,c,d"
print(s.split(","))

s=["a""b""c"]
w=",".join(s)
print(w)

s="abcdef"
print(s[0:6:2])

s="banana"
print(s.replace("a","@"))

s="hello123"
print(s.isalnum())

s="python"
print(s.capitalize())

s="hello world"
print(s.title())

s="python"
r=(s.replace("a","").replace("e","").replace("i","").replace("o","").replace("u",""))
print(r)

s="madam"
print(s[::-1])
