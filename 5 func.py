def output(x):   # Defination of function
    for i in x:
        print(i)
x=["kavita","meena","teena"]
output(x) #Calling of function

#Function with argument
print("\nFunction with argument:")
def add(x,y):
    return x+y
def do_twice(func,x,y):
    return func(func(x,y),func(x,y))
a=5
b=10
print(do_twice(add,a,b))

#lambda
print("LAMBDA")
print((lambda x:x**2+5*x+4)(-4))

#lambda func
add=lambda x,y:x+y
print(add(2,3))
