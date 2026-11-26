import re

#text="hello world"
#print(re.search(r"world",text))

#text="hello world"
#print(re.match(r"hello",text))
#print(re.match(r"world",text))

#text="i have 2 apples and 5 oranges"
#print(re.findall(r"\d+",text))

#text="the price is 45 dollars,30 cents and 50 rupees."
#print(re.findall(r"\d+",text))

#text="i have 2 apples and 5 oranges."
#for match  in re.finditer(r"\d+",text):
#    print(match.group(),"at",match.start())

#ext="hello 123,welcome 456!"
#rint(re.sub(r"\d+","number",text))

#ext="apple,orange;banana,grape"
#rint(re.split(r"[;,]",text))
#ext="john:34,alice:45,bob:23"
#rint(re.findall(r"(\w+):(\d+)",text))

#pattern=re.compile(r"\d+")
#text="123 apples and 456 oranges"
#print(pattern.findall(text))

#text="HELLO world"
#print(re.search(r"hello",text,re.IGNORECASE))

#text="""first line
#second line
#third line"""
#print(re.findall(r"^s\w+",text,re.MULTILINE))

#text="hello\nworld"
#print(re.search(r"hello.*world",text))
#print(re.search(r"hello.*world",text,re.DOTALL))

#email="user@example.com"
#if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$",email):
#    print("valid email")
#else:
#    print("invalid email")

#text="price:$123.45"
#print(re.sub(r"[^0-9.]","",text))

#tweet="excited for #python3 and following @openai!"
#print(re.findall(r"#\w+",tweet))
#print(re.findall(r"@\w+",tweet))

#text="card: 1234-5678-9012-3456"
#print(re.sub(r"\d{4}-\d{4}-\d{4}","****-****-****-****",text))
