def abcd(func):
    def wrapper():
        print("before eating add sprinklers")
        func()
        print("after eating icecream")
    return wrapper

@abcd
def icecream():
    print("eating ice cream")
icecream()
